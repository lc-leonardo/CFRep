# CFRep

## Introduction to the dataset
CFRep is an open-access video dataset designed for rep-based exercise validation for functional fitness settings. The dataset attempts to alleviate the limited quantity of free access, carefully labeled data for movement evaluation quality and repetition accuracy inside functional fitness scenarios.

## Data Preparation
To prepare the data, we recorded the videos in three distinct camera angles, to achieve a complete angle distinction, such as front, diagonal, and side, emulating the point-of-view conditions present in competitions.
The deadlift was selected due to frequent debates within the community. Additionally, the use of barbells can challenge pose estimation models, depending on the recording angle. Squat was also chosen because of frequent contesting, along with a cleaner execution, which opened a way to improve our comprehension of the angle variations. And double-unders, due to their coordination difficulty, and their frequent presence in fitness competitions. To enhance the utility and organization of our dataset, the videos were trimmed and labeled for clear identification between the categories we evaluated.

## Annotation Collection
The annotation collection process involved labeling each repetition in raw exercise videos as either valid (1) or invalid (0), following the official functional fitness rulebook. Annotations are performed by a certified CrossFit Judge and L1 Trainer with 1.5 years of coaching experience. According to the rulebook, a deadlift is marked as invalid if (1) the barbell does not start from the ground, (2) the lift is not completed with full hip and knee extension, or (3) the athlete intentionally bounces the plates. An air squat is valid if (1) the hips do not descend below the knees, or (2) the movement lacks full extension at the top. A double under is invalid if the rope fails to pass under the feet twice during a single jump.

## Dataset Statistics
CFRep comprises 64 videos, which we collected from eight participants (4 male, 4 female), performing three exercise types, in three different camera angles, containing 258 reps for deadlift, 328 reps for double-unders, and 270 reps for squat. Reps inside each video range from 10 to 25, including valid and invalid. Each of the repetitions was annotated as rep or no-rep individually using criteria aligned with official judging standards. To support all detailed labeling, we implemented a rep-wise annotation in a CSV file inside a rep label field, enabling evaluation of accuracy classification parameters such as accuracy, precision, recall, and F1-score.

## Dataset Properties
This dataset was developed to evaluate rep-validation systems under challenging conditions that have properties such as variance in the angles, inter-subject biomechanics, and execution degradation due to fatigue. CFRep will be able to contribute to the development of studies in the area of assessing the quality of exercises, automated judging systems, and lightweight fitness tracking on edge devices.
