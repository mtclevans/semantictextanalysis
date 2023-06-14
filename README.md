2. IMPORT FRAMEWORK DEPENDENCIES ...?


**PL-Marker Evaluation Scripts**
1. Ensure evaluation scripts for PL-marker are used following the PL-Marker setup guide: https://github.com/thunlp/PL-Marker#Setup
2. Import all PL-Marker model dependencies, including the requirement.txt and custom Transformers file https://github.com/thunlp/PL-Marker#Install-dependencies
3. Ensure the Scibert pre-trained model is imported according to the PL-Marker setup file: https://github.com/thunlp/PL-Marker#Trained-Models
4. Ensure the Scierc dataset is uploaded https://github.com/thunlp/PL-Marker#download-and-preprocess-the-datasets
5. Ensure the Runtime type is set to GPU for consistency with the original PL-Marker experiment
6. Use the PL-Marker QuickStart to evaluate the pre-trained PL-Marker models run_acener.py and  run_re.py for Scierc: https://github.com/thunlp/PL-Marker#quick-start

**Semantic Text Analysis Framework**

**Python**
1. Import all required functions for the framework (framework/functions)
2. Undertake analysis on the Scierc dataset distribution (framework/sciercanalysis)
3. Undertaken confusion matrix analysis for ner and re (framework/confusionmatrices)
4. Generate POS Tags for Qualitative Data Analysis Software import (framework/posTags)
5. Transform data and generate .xlsx for Qualitative Data Analysis Software import (framework/qdas/dataTransform)

**Qualitative Data Analysis**
We used Nvivio (REF) on Windows OS.
Please note: Not all Nvivo features are present on MacOS:
Queries will produce different results on Mac as they are not filtered by user.
Two users annotated relations to generate a Kappa score.
- Cluster Analysis and Pearson’s Correlation Coefficient (MacOS only)
- Filter queries by user (MacOS only)
For more information see: https://help-nv.qsrinternational.com/20/mac/Content/projects-teamwork/work-with-projects-windows-mac.htm

**Semantic Text Analysis Process**
1. Import exported .xlsx file into Nvivo
2. Undertake Text Analysis using the codebooks provided in framework/codebooks.md
Note: We annotated all themes twice to generate a Kappa statistic.

**Results**
1. PL-Marker model F1 scores and standard deviation can be found in results/pl-marker.md
2. Database statistics can be found in results/sciercStatistics.md (Data -> Files -> SCIERC QDAS Import File - PART-OF & FEATURE-OF)
3. Confusion matrices can be found in results/confusionMatrices
4. The Nvivo file for the Semantic Text Analysis annotations undertaken in this research can be found in
- Queries for theme co-occurence and validation are present in this Nvivo file under Explore -> Queries -> Query Criteria
- Please note: These results will not match the research when running on MacOS.
- Query results for theme co-occurence and validation are present in this Nvivo file under Explore -> Queries -> Query Results
- Please note: These results will not match the research when running on MacOS.
- Kappa statistics can be found INSERT.
- Pearson's Correlation Coefficients must be regenerated at runtime. Please navigate to: Explore -> Diagrams -> Cluster Analysis -> Select codes and click ‘next’ -> Select all codes -> Click ‘Finish’ -> Navigate to ‘Summary’ -> Right-click and ‘Export list’
- Please note: This feature is not available in MacOS


ADD RESULTS - CORRELATION COEFFICIENT EXPORTS, THEME COOCCURENCE EXPORTS, VALIDATION QUERY RESULTS, QUERY RESULTS (=THEME COOCCURENCES)
