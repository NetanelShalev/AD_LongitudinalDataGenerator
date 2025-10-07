# Pitt Corpus Linguistic Analysis Project

## Overview
This project applies 9 linguistic feature extraction functions from the `multi_file_analysis.ipynb` notebook to the Pitt corpus dataset for Alzheimer's Disease (AD) research. The analysis extracts linguistic features that may be indicative of cognitive decline.

## Files Created

### 1. `pitt_linguistic_analysis.py`
Main analysis script that processes the Pitt corpus data and extracts linguistic features.

**Features extracted:**
1. **noun_token_ratio** - Proportion of noun POS tokens among cleaned tokens
2. **hapax_legomena_ratio** - Proportion of words occurring exactly once
3. **low_freq_word_ratio** - Proportion of words occurring ≤2 times
4. **brunet_index** - Brunet's index of lexical diversity
5. **type_token_ratio** - Type-Token Ratio (lexical diversity)
6. **adposition_ratio** - Proportion of prepositions/adpositions
7. **unigram_bigram_count** - Count of unique unigrams and bigrams
8. **subtlex_frequency** - Mean SUBTLEX word frequency
9. **zipf_frequency** - Mean Zipf word frequency

### 2. `pitt_corpus_linguistic_features.csv`
Output dataset containing:
- All original Pitt corpus data (517 records, 281 unique patients)
- 9 new linguistic feature columns
- Ready for machine learning and statistical analysis

### 3. `pitt_analysis_summary.py`
Analysis script that provides:
- Descriptive statistics by diagnosis group
- Statistical comparisons between Control and ProbableAD groups
- Feature correlation analysis
- Practical usage examples

## Dataset Structure

### Original Columns (7):
- `uuid` - Unique identifier for each record
- `patient_id` - Patient identifier
- `visit_num` - Visit number for longitudinal data
- `age` - Patient age at time of recording
- `gender` - Patient gender
- `text` - Cookie theft picture description text
- `gold_diagnosis` - Clinical diagnosis

### New Feature Columns (9):
- `noun_token_ratio` - Noun frequency measure
- `hapax_legomena_ratio` - Lexical diversity measure
- `low_freq_word_ratio` - Low-frequency word usage
- `brunet_index` - Lexical richness index
- `type_token_ratio` - Vocabulary diversity
- `adposition_ratio` - Grammatical complexity
- `unigram_bigram_count` - Text complexity measure
- `subtlex_frequency` - Word frequency (corpus-based)
- `zipf_frequency` - Word frequency (Zipf distribution)

## Key Findings

### Diagnostic Group Differences (Control vs ProbableAD):
1. **Noun Token Ratio**: Significantly higher in controls (p<0.001, Cohen's d=0.428)
2. **Adposition Ratio**: Significantly higher in controls (p<0.001, Cohen's d=0.396)
3. **Hapax Legomena Ratio**: Significantly higher in controls (p=0.023, Cohen's d=0.216)
4. **SUBTLEX Frequency**: Significantly higher in controls (p=0.029, Cohen's d=0.207)

### Most Discriminative Features:
1. Noun token ratio (Cohen's d = 0.428)
2. Adposition ratio (Cohen's d = 0.396)
3. Hapax legomena ratio (Cohen's d = 0.216)
4. SUBTLEX frequency (Cohen's d = 0.207)

### Sample Sizes by Diagnosis:
- Control: 232 records
- ProbableAD: 217 records
- MCI: 42 records
- PossibleAD: 18 records
- Other diagnoses: 8 records

### Longitudinal Data:
- 137 patients have multiple visits
- Enables analysis of linguistic changes over time

## Usage Examples

### Load the dataset:
```python
import pandas as pd
df = pd.read_csv('pitt_corpus_linguistic_features.csv')
```

### Basic analysis:
```python
# Compare groups
control_group = df[df['gold_diagnosis'] == 'Control']
ad_group = df[df['gold_diagnosis'] == 'ProbableAD']

# Feature comparison
feature_cols = ['noun_token_ratio', 'hapax_legomena_ratio', 'adposition_ratio']
control_group[feature_cols].mean()
ad_group[feature_cols].mean()
```

### Longitudinal analysis:
```python
# Patients with multiple visits
multi_visit = df.groupby('patient_id')['visit_num'].count()
longitudinal_patients = multi_visit[multi_visit > 1].index

# Track changes over time
patient_data = df[df['patient_id'] == longitudinal_patients[0]].sort_values('visit_num')
```

## Dependencies
- pandas
- numpy
- nltk
- tqdm
- scipy
- textblob
- matplotlib
- seaborn

## Execution
Run the analysis:
```bash
python pitt_linguistic_analysis.py
```

Run the summary analysis:
```bash
python pitt_analysis_summary.py
```

## Research Applications
This dataset is suitable for:
1. AD classification/prediction models
2. Longitudinal cognitive decline analysis
3. Age-related linguistic change studies
4. Gender difference investigations
5. Correlation with cognitive test scores
6. Feature selection for ML models
7. Linguistic marker identification

The extracted features provide a comprehensive linguistic profile that can be used to study language changes associated with Alzheimer's disease and other forms of cognitive decline.