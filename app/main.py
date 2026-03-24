from fastapi import FastAPI
import uvicorn

# Initialize FastAPI app
# MuleSoft-inspired API Management & Data Transformation Toolkit
app = FastAPI(
    title="MuleSoft-like API Toolkit",
    description="Python-based toolkit for Data Transformation (JSON, CSV, XML) and API Management",
    version="1.0.0"
)

from .data_transformer import DataTransformer
from typing import Dict, Any, List, Union
from fastapi import Body

@app.post("/transform", tags=["Transformation"])
async def transform_data(
    input_format: str = Body(..., title="Input Format", examples=["json", "csv", "xml"]),
    output_format: str = Body(..., title="Output Format", examples=["json", "csv", "xml"]),
    payload: Union[str, List[Dict], Dict] = Body(..., title="Data to Transform")
):
    """
    Endpoint to transform data between different formats.
    Supported: JSON to CSV/XML, CSV to JSON, XML to JSON.
    """
    try:
        # Step 1: Handle input conversion to JSON/Dict
        if input_format.lower() == "json":
            data = payload
        elif input_format.lower() == "csv":
            data = DataTransformer.csv_to_json(str(payload))
        elif input_format.lower() == "xml":
            data = DataTransformer.xml_to_json(str(payload))
        else:
            return {"error": f"Unsupported input format: {input_format}"}

        # Step 2: Handle output conversion
        if output_format.lower() == "json":
            result = data
        elif output_format.lower() == "csv":
            result = DataTransformer.json_to_csv(data)
        elif output_format.lower() == "xml":
            result = DataTransformer.json_to_xml(data)
        else:
            return {"error": f"Unsupported output format: {output_format}"}

        return {
            "status": "success",
            "from": input_format,
            "to": output_format,
            "result": result
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/health", tags=["Monitoring"])
async def health_check():
    """
    Basic health check endpoint to verify API status.
    API ki health check karne ke liye basic endpoint.
    """
    return {
        "status": "healthy",
        "project": "project2-mulesoft-like",
        "message": "API Toolkit is running smoothly!"
    }

if __name__ == "__main__":
    # Start the server locally for testing
    uvicorn.run(app, host="127.0.0.1", port=8000)
