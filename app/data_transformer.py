import pandas as pd
import json
import xmltodict
import io
from typing import Any, Dict, List, Union

class DataTransformer:
    """
    MuleSoft-inspired Data Transformer Toolkit.
    Mimics DataWeave logic for format conversion and data handling.
    """

    @staticmethod
    def json_to_csv(json_data: Union[str, List[Dict]]) -> str:
        """
        Converts JSON data to CSV string.
        JSON data ko CSV format mein convert karein.
        """
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        
        df = pd.DataFrame(json_data)
        return df.to_csv(index=False)

    @staticmethod
    def csv_to_json(csv_data: str) -> List[Dict]:
        """
        Converts CSV string to List of Dictionaries (JSON-like).
        CSV data ko JSON format (list of dicts) mein convert karein.
        """
        df = pd.read_csv(io.StringIO(csv_data))
        return df.to_dict(orient="records")

    @staticmethod
    def json_to_xml(json_data: Union[str, Dict], root_name: str = "root") -> str:
        """
        Converts JSON/Dict to XML string.
        JSON ko XML format mein convert karein.
        """
        if isinstance(json_data, str):
            json_data = json.loads(json_data)
        
        # xmltodict requires a single root element
        xml_dict = {root_name: json_data}
        return xmltodict.unparse(xml_dict, pretty=True)

    @staticmethod
    def xml_to_json(xml_data: str) -> Dict:
        """
        Converts XML string to Dictionary.
        XML data ko JSON/Dict format mein convert karein.
        """
        return xmltodict.parse(xml_data)

# Example usage (for local testing):
if __name__ == "__main__":
    sample_json = [{"id": 1, "name": "Item A"}, {"id": 2, "name": "Item B"}]
    
    # Test JSON to CSV
    csv_result = DataTransformer.json_to_csv(sample_json)
    print("CSV Result:\n", csv_result)
    
    # Test JSON to XML
    xml_result = DataTransformer.json_to_xml(sample_json[0], root_name="Item")
    print("\nXML Result:\n", xml_result)
