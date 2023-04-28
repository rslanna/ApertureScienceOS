from .constants import PATH_TO_LANGUAGE_JSON_FILES
import os, json

class ApertureTranslator:

    def __init__(self, language):
        self.language = language
        self.language_json = self.load_language()

    def load_language(self):
        for file_name in [file for file in os.listdir(PATH_TO_LANGUAGE_JSON_FILES) if file.endswith('.json')]:
            if self.language in file_name:
                with open(PATH_TO_LANGUAGE_JSON_FILES + file_name) as json_file:
                    data = json.load(json_file)
                    return data
                
    def get_command_response_and_delay(self, command):
        for item in self.language_json["commands"]:
            if item["user_command"] == command:
                errors = item["errors"] if "errors" in item else None
                return (item["time_between_each_response"], item["response"], errors)
            
        return None

    def get_start_loading_text(self):
        return self.language_json["start_loading_text"]
    
    def get_translation_for(self, field):
        return self.language_json[field]
