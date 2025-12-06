import json
from ocr import extract_text_from_image, extract_text_from_pdf
from extractor import extract_fields
from carbon_calculator import compute_carbon

def lambda_handler(event, context):
    try:
        # API Gateway proxy: body is a JSON string
        body = event.get("body")
        if isinstance(body, str):
            body = json.loads(body)
        elif body is None:
            body = {}

        # text comes from Streamlit frontend
        text = body.get("text", "")

        if not text:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "Missing 'text' in request body"})
            }

        # Call Cloudflare + carbon calculator
        fields = extract_fields(text)
        carbon = compute_carbon(fields)

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "fields": fields,
                "carbon": carbon
            }),
            "isBase64Encoded": False
        }

    except Exception as e:
        # Log error for CloudWatch debugging
        print("Error in lambda_handler:", str(e))
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": "Internal error in Lambda"}),
            "isBase64Encoded": False
        }

