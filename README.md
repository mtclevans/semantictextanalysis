<h1>PL-Marker Evaluation Scripts</h1>
<em>The following PL-Marker setup guide provides a pre-trained model and subsequent evaluation scripts: https://github.com/thunlp/PL-Marker#Setup</em>
<br>
1. Import PL-Marker trained models for SciERC NER and RE: https://github.com/thunlp/PL-Marker#Trained-Models<br>
2. Import SciBERT pre-trained model dependencies: https://github.com/thunlp/PL-Marker#training-script<br>
3. Import PL-Marker model dependencies: requirement.txt and custom Transformers file https://github.com/thunlp/PL-Marker#Install-dependencies<br>
4. Upload SciERC dataset: https://github.com/thunlp/PL-Marker#download-and-preprocess-the-datasets<br>
  Note: Ensure the data dir matches the evaluation script: https://github.com/thunlp/PL-Marker#quick-start<br>
6. Ensure the Runtime type is set to GPU for consistency with the original PL-Marker experiment<br>
7. Use the PL-Marker QuickStart to evaluate the pre-trained PL-Marker NER model for SciERC: https://github.com/thunlp/PL-Marker#quick-start<br>
   Note: Ensure you have created the output dir within the evaluation script: https://github.com/thunlp/PL-Marker#quick-start<br>
8. Use the PL-Marker QuickStart to evaluate the pre-trained PL-Marker RE model run_re.py for SciERC: https://github.com/thunlp/PL-Marker#quick-start<br>
   Note: Ensure you have created the output dir within the evaluation script: https://github.com/thunlp/PL-Marker#quick-start

<h1>Semantic Text Analysis Framework</h1>

<h2>Python</h2>
1. Import framework dependencies: pandas, NLTK, matplotlib.pyplot, sklearn.metrics.ConfusionMatrixDisplay<br>
2. Import all required functions for the framework (framework/functions.py)<br>
3. Undertake analysis on the Scierc dataset distribution (framework/sciercanalysis)<br>
4. Undertaken confusion matrix analysis for ner and re (framework/confusionmatrices)<br>
5. Generate POS Tags for Qualitative Data Analysis Software import (framework/posTags.py)<br>
6. Transform data and generate .xlsx for Qualitative Data Analysis Software import (framework/qdas/dataTransform.py)

<h2>Semantic Text Analysis</h2>
<em>We used Nvivio (REF) on Windows OS.</em><br>
<em>Two users annotated relations to generate a Kappa score.</em><br>
<em>Please note: Not all Nvivo features are present on MacOS:</em><br>
<em>1. Queries will produce different results on Mac OS as they are not filtered by user.</em><br>
<em>2. Cluster Analysis and Pearson’s Correlation Coefficient (WindowsOS only)</em><br>
<em>For more information see: https://help-nv.qsrinternational.com/20/mac/Content/projects-teamwork/work-with-projects-windows-mac.htm</em><br><br>
1. Import exported qdas.xlsx file into Nvivo<br>
2. Undertake Text Analysis using the codebooks provided in framework/codebooks.md
Note: We annotated all themes twice to generate a Kappa statistic.

<h1>Results</h1>
1. PL-Marker model F1 scores and standard deviation can be found in results/pl-marker.md<br>
2. Database statistics can be found in results/sciercStatistics.md (Data -> Files -> SCIERC QDAS Import File - PART-OF & FEATURE-OF)<br>
3. Confusion matrices can be found in results/confusionMatrices<br>
4. The Nvivo file for the Semantic Text Analysis annotations undertaken in this research can be found in results/Nvivo Semantic Text Analysis WindowsOS.nvp<br>
- Queries for theme co-occurence and validation are present in this Nvivo file under Explore -> Queries -> Query Criteria<br>
- Please note: These results will not match the research when running on MacOS.<br>
- Query results for theme co-occurence and validation are present in this Nvivo file under Explore -> Queries -> Query Results<br>
- Please note: These results will not match the research when running on MacOS.<br>
- Kappa statistics can be found results/kappa.md<br>
- Pearson's Correlation Coefficients must be regenerated at runtime. Please navigate to: Explore -> Diagrams -> Cluster Analysis -> Select codes and click ‘next’ -> Select all codes -> Click ‘Finish’ -> Navigate to ‘Summary’ -> Right-click and ‘Export list’<br>
- <em>Please note: This feature is not available in MacOS</em>
