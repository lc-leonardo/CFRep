# CFRep

## Introduction to the dataset
CFRep is an open-access video dataset designed for rep-based exercise validation for functional fitness settings. The dataset attempts to alleviate the limited quantity of free access, carefully labeled data for movement evaluation quality and repetition accuracy inside functional fitness scenarios.

## Data Preparation

- Recorded videos in three distinct camera angles: front, diagonal, and side.
- Emulated point-of-view conditions present in competitions.
- **Deadlift**:
  - Selected due to frequent debates in the community.
  - Barbell use challenges pose estimation models depending on the angle.
- **Squat**:
  - Chosen for frequent contesting and cleaner execution.
  - Helped improve comprehension of angle variations.
- **Double-unders**:
  - Chosen for coordination difficulty and frequent presence in fitness competitions.
- Videos were trimmed and labeled for clear identification between evaluated categories.

## Annotation Collection

- Labeled each repetition as valid (1) or invalid (0) based on the official functional fitness rulebook.
- Annotations performed by a certified CrossFit Judge and L1 Trainer with 1.5 years of coaching experience.
- **Deadlift invalid if**:
  - Barbell does not start from the ground.
  - Lift is not completed with full hip and knee extension.
  - Athlete intentionally bounces the plates.
- **Air squat invalid if**:
  - Hips do not descend below the knees.
  - Movement lacks full extension at the top.
- **Double under invalid if**:
  - Rope fails to pass under the feet twice during a single jump.

## Dataset Statistics

- CFRep comprises **64 videos**.
- Data collected from **8 participants** (4 male, 4 female).
- Exercises: **deadlift, double-unders, squat**.
- Three different camera angles used.
- Total repetitions:
  - **258 deadlift**
  - **328 double-unders**
  - **270 squat**
- Each video: 10 to 25 reps, both valid and invalid.
- Each rep annotated individually as **rep** or **no-rep**.
- Annotations follow official judging standards.
- Rep-wise annotation stored in a CSV `rep label` field.
- Enables evaluation using metrics: **accuracy, precision, recall, F1-score**.

## Dataset Properties

- Developed to evaluate rep-validation systems under challenging conditions.
- Key properties:
  - **Variance in camera angles**
  - **Inter-subject biomechanics**
  - **Execution degradation due to fatigue**
- Supports:
  - Studies on exercise quality assessment.
  - Automated judging systems.
  - Lightweight fitness tracking on edge devices.
