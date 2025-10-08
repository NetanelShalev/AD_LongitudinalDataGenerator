import os
import glob
import json

def load_json_files_from_folder(folder_path):
    """Load all JSON files from a specified folder."""
    json_files = glob.glob(os.path.join(folder_path, "*.json"))
    all_data = []

    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                all_data.append(data)
                character_name = data.get('name', 'Unknown')
                start_deterioration_age = data.get(
                    'start_deterioration_age', 'Unknown')
                print(
                    f"Loaded: {os.path.basename(file_path)} - Character: {character_name} - Start deterioration age: {start_deterioration_age}")
        except Exception as e:
            print(f"Error loading {file_path}: {e}")

    return all_data


def aggregate_stories_with_years_before_diagnostic(all_character_data):
    """
    Combine all stories from all characters and calculate years before diagnostic.
    Each story becomes a data point with its years before diagnostic based on individual character's start_deterioration_age.
    """
    all_story_points = []

    for character_data in all_character_data:
        character_name = character_data.get('name', 'Unknown')
        stories = character_data.get('stories', [])
        deterioration_age = character_data.get('start_deterioration_age')

        if deterioration_age is None:
            print(
                f"Warning: No deterioration age found for {character_name}, skipping...")
            continue

        for story_data in stories:
            age = story_data.get('age')
            story = story_data.get('story', '')
            if age is not None and story:
                years_before_diagnostic = -(deterioration_age - age)
                all_story_points.append({
                    'character': character_name,
                    'age': age,
                    'deterioration_age': deterioration_age,
                    'years_before_diagnostic': years_before_diagnostic,
                    'story': story
                })

    return all_story_points

__all__ = [
    "load_json_files_from_folder",
    "aggregate_stories_with_years_before_diagnostic"
]