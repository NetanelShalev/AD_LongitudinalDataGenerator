# AD Longitudinal Data Generator & Linguistic Analysis

A lightweight research workspace for generating, organizing, and analyzing synthetic longitudinal narrative data related to Alzheimer’s Disease (AD) progression and healthy aging. The repository contains:
- Synthetic persona definitions (baseline attributes & deterioration onset age)
- Generated story timelines (retellings at different ages, pre‑ and post‑deterioration)
- Linguistic feature extraction & exploratory analysis (lexical diversity, POS ratios, frequency metrics)
- Early paper assets and chat interaction modes for iterative exploration

## 🎯 Objective
Model and explore longitudinal linguistic signals that may correlate with cognitive decline. The current focus: per‑story metrics vs. "years before diagnostic" (individualized by each persona's deterioration onset age) to visualize potential trends.

## 📂 Repository Structure
| Folder / File | Description |
| ------------- | ----------- |
| `personas/` | JSON persona profiles (name, demographics, `start_deterioration_age`, and optionally other metadata). Serves as the seed for generating longitudinal story timelines. |
| `stories/` | Generated longitudinal narrative data grouped by generation batches (e.g., `data_06_07`, `data_31_07`, `data_aug_10`). Subfolders separate cohorts: `dementia`, `aging`, `healthy_data`, etc. Each JSON file = one persona’s stories across ages. |
| `stories/*/dementia/` | Primary dataset used in current notebook analyses. Each file includes: persona name, deterioration onset age, and an array of `{age, story}` entries. |
| `stories/*/aging/` | (Placeholder / future) Non‑dementia aging trajectories for contrastive modeling. |
| `stories/*/healthy_data/` | Healthy control narratives (no deterioration) for baselines. |
| `multi_file_analysis.ipynb` | Main exploratory notebook: loads dementia narratives, normalizes ages to "years before diagnostic", computes multiple linguistic metrics, and visualizes scatter plots with regression + correlation stats. |
| `subtl_and_zipf.csv` | External lexical frequency reference (SUBTLEX US + Zipf scale) used to weight token frequency metrics. |
| `.github/chatmodes/` | Prompt presets (e.g., "Dementia deterioration", "Healthy-aging") used to steer generation style. Helpful for reproducible synthetic data regimes. |
| `paper/` | Draft artifacts (PDF, presentation, key notes) documenting background, rationale, and preliminary findings. |
| `test.txt` | Scratch / placeholder file (safe to ignore or remove). |
| `README.md` | You are here. |

## 🧪 Current Linguistic Metrics (Notebook)
Implemented in `multi_file_analysis.ipynb`:
- Noun Token Ratio (NN, NNS, NNP, NNPS / total POS‑tagged tokens)
- Hapax Legomena Ratio (types occurring once / tokens)
- Low-Frequency (≤2) Ratio
- Brunet Index (lexical richness)
- Type–Token Ratio (TTR)
- Adposition Ratio (IN [+ TO])
- Unigram + Bigram Repetition Proxy (unique unigrams + bigrams count)
- SUBTLEX Weighted Frequency (mean weighted by SUBTLWF)
- Zipf Weighted Frequency (mean weighted by Zipf value)

Each metric is plotted against `years_before_diagnostic` with:
- Per‑persona color coding
- Linear regression trend line
- Pearson r, p-value, and significance stars

## 🗃 Data Model (Persona Story File)
Example (abridged):
```json
{
  "name": "Jane Doe",
  "start_deterioration_age": 67,
  "stories": [
    {"age": 55, "story": "..."},
    {"age": 60, "story": "..."},
    {"age": 66, "story": "..."},
    {"age": 69, "story": "..."}
  ]
}
```
Derived field inside the notebook: `years_before_diagnostic = -(start_deterioration_age - age)` (so negative values represent years prior to deterioration onset; values ≥ 0 are at/after onset).

## ⚙️ Environment & Dependencies
Minimal Python environment (≥3.9) suggestions:
```
pip install numpy pandas matplotlib scipy textblob nltk
```
One-time NLTK data downloads performed in the notebook (`stopwords`, `punkt`, `averaged_perceptron_tagger`). If running scripts headlessly, add:
```python
import nltk
for pkg in ["stopwords", "punkt", "averaged_perceptron_tagger"]:
    nltk.download(pkg)
```
Optional: cache large frequency CSV externally if versioning strategy changes.

## 🚀 How to Run the Analysis
1. Place / update persona story JSONs under the latest `stories/<batch>/dementia/` directory.
2. Open `multi_file_analysis.ipynb` and run all cells.
3. Inspect printed load summaries (ensures deterioration ages present).
4. Review per‑metric scatter plots for emerging trends / potential markers.

### The prompt for the agent:
Read the file carfully. Understand the core memory and the preson. Create the retellings by the the exact instructions you got. 
