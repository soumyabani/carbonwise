import json
from ocr import extract_text_from_image, extract_text_from_pdf
from extractor import extract_fields
from carbon_calculator import compute_carbon

def lambda_handler(event, context):
    # receive text (already extracted by Streamlit) or file content
    text = event["text"]

    fields = extract_fields(text)
    carbon = compute_carbon(fields)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "fields": fields,
            "carbon": carbon
        })
    }

