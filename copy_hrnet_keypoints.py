#!/usr/bin/env python3
"""
Script to copy HRNet keypoint files from judge_runs_HB to CFRep/json_keypoints
with proper naming and label updates.
"""

import os
import json
import shutil
from pathlib import Path

# Define the video name mappings (old -> new)
VIDEO_RENAMES = {
    # Double-unders renames
    "double-unders_diag_m1_12_2": "double-unders_diag_m1_12_3",
    "double-unders_diag_m2_8_7": "double-unders_diag_m2_9_7",
    "double-unders_front_m2_11_1": "double-unders_front_m2_12_2",
    "double-unders_front_m4_14_1": "double-unders_front_m4_14_2",
    "double-unders_front_w2_12_1": "double-unders_front_w2_13_1",
    "double-unders_side_m1_12_2": "double-unders_side_m1_13_2",
    "double-unders_side_m4_11_6": "double-unders_side_m4_11_7",
    "double-unders_side_w2_10_3": "double-unders_side_w2_11_3",
    "double-unders_side_w4_15_9": "double-unders_side_w4_15_10",
    # Squat renames
    "squat_diag_m4_6_6": "squat_diag_m4_5_7",
    "squat_side_m4_12_0": "squat_side_m4_11_1",
    # Double-unders additional rename
    "double-unders_diag_w2_6_4": "double-unders_diag_w2_6_5",
}

# Base paths
BASE_PATH = Path("/media/lori/easystore")
JUDGE_RUNS_HB = BASE_PATH / "judge_runs_HB"
CFREP_PATH = BASE_PATH / "CFRep" / "CFRep"
JSON_KEYPOINTS_PATH = CFREP_PATH / "json_keypoints"
VIDEO_CONFIG_PATH = CFREP_PATH / "video_config.json"

# Model name
HRNET_MODEL = "hrnet-w48_dark-8xb32-210e_coco-wholebody-384x288"

def load_video_config():
    """Load the video_config.json to get binary labels."""
    with open(VIDEO_CONFIG_PATH, 'r') as f:
        return json.load(f)

def get_binary_label(video_config, video_name):
    """Get binary label for a video from config."""
    for entry in video_config:
        if entry['filename'] == f"{video_name}.mp4":
            return entry['binary_label']
    return None

def process_keypoint_file(src_file, dst_file, video_name, binary_label):
    """Copy and update a keypoint JSON file with correct labels and video path."""
    with open(src_file, 'r') as f:
        data = json.load(f)
    
    # Update binary_label and video_path
    data['binary_label'] = binary_label
    data['video_path'] = f"CFRep/{video_name}.mp4"
    
    # Write updated JSON
    with open(dst_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"  ✓ Copied and updated: {dst_file.name}")

def copy_hrnet_keypoints():
    """Main function to copy HRNet keypoint files."""
    video_config = load_video_config()
    exercises = ["deadlift", "double_unders", "squat"]
    
    total_copied = 0
    total_skipped = 0
    missing_labels = []
    
    for exercise in exercises:
        print(f"\n{'='*70}")
        print(f"Processing {exercise.upper()}")
        print(f"{'='*70}")
        
        # Source directory
        src_exercise_dir = JUDGE_RUNS_HB / exercise / HRNET_MODEL
        
        if not src_exercise_dir.exists():
            print(f"⚠ Source directory not found: {src_exercise_dir}")
            continue
        
        # Get all video folders
        video_folders = [d for d in src_exercise_dir.iterdir() if d.is_dir()]
        
        for video_folder in sorted(video_folders):
            old_video_name = video_folder.name
            
            # Apply rename mapping if exists
            new_video_name = VIDEO_RENAMES.get(old_video_name, old_video_name)
            
            # Get binary label
            binary_label = get_binary_label(video_config, new_video_name)
            
            if binary_label is None:
                print(f"\n⚠ No binary label found for: {new_video_name}")
                missing_labels.append(new_video_name)
                total_skipped += 1
                continue
            
            print(f"\n{new_video_name}")
            if old_video_name != new_video_name:
                print(f"  (renamed from: {old_video_name})")
            print(f"  Binary label: {binary_label}")
            
            # Find the topdown JSON file (shorter name)
            json_files = list(video_folder.glob("*_topdown.json"))
            
            if not json_files:
                print(f"  ⚠ No topdown JSON file found in {video_folder}")
                total_skipped += 1
                continue
            
            src_json = json_files[0]
            
            # Destination directory
            dst_dir = JSON_KEYPOINTS_PATH / exercise / new_video_name
            dst_dir.mkdir(parents=True, exist_ok=True)
            
            # New filename following the pattern
            dst_filename = f"{new_video_name}_hrnet-w48_dark-8xb32-210e_coco-wholebody-384x288.json"
            dst_json = dst_dir / dst_filename
            
            # Copy and update the file
            try:
                process_keypoint_file(src_json, dst_json, new_video_name, binary_label)
                total_copied += 1
            except Exception as e:
                print(f"  ✗ Error processing {src_json}: {e}")
                total_skipped += 1
    
    # Summary
    print(f"\n{'='*70}")
    print(f"SUMMARY")
    print(f"{'='*70}")
    print(f"Total files copied: {total_copied}")
    print(f"Total files skipped: {total_skipped}")
    
    if missing_labels:
        print(f"\nVideos with missing labels:")
        for video in missing_labels:
            print(f"  - {video}")

if __name__ == "__main__":
    print("Starting HRNet keypoint files migration...")
    copy_hrnet_keypoints()
    print("\n✓ Migration complete!")
