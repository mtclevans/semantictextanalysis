<h1>PL-Marker Evaluation Scripts</h1>
<em>The  <a href="https://github.com/thunlp/PL-Marker#Setup" target="_blank">PL-Marker setup guide</a> provides a pre-trained model and subsequent evaluation scripts</em>
<br>
1. <a href="https://github.com/thunlp/PL-Marker#Trained-Models" target="_blank">Import PL-Marker trained models</a> for SciERC NER and RE<br>
2. Import SciBERT pre-trained model <a href="https://github.com/thunlp/PL-Marker#training-script" target="_blank"> dependencies</a><br>
3. Import PL-Marker model <a href="https://github.com/thunlp/PL-Marker#Install-dependencies" target="_blank"> dependencies</a>: requirement.txt and custom Transformers file<br>
4. <a href="https://github.com/thunlp/PL-Marker#download-and-preprocess-the-datasets" target="_blank"> Upload SciERC dataset</a><br>
  <em>Note: Ensure the data dir matches the <a href="https://github.com/thunlp/PL-Marker#quick-start" target="_blank"> evaluation script</a></em><br>
6. Ensure the Runtime type is set to GPU for consistency with the original PL-Marker experiment<br>
7. Use the <a href="https://github.com/thunlp/PL-Marker#quick-start" target="_blank">PL-Marker QuickStart</a> to evaluate the pre-trained PL-Marker NER model for SciERC<br>
   <em>Note: Ensure you have created the output dir within the <a href="https://github.com/thunlp/PL-Marker#quick-start" target="_blank">evaluation script</a></em><br>
8. Use the <a href="https://github.com/thunlp/PL-Marker#quick-start" target="_blank">PL-Marker QuickStart</a> to evaluate the pre-trained PL-Marker RE model run_re.py for SciERC<br>
   <em>Note: Ensure you have created the output dir within the <a href="https://github.com/thunlp/PL-Marker#quick-start" target="_blank">evaluation script</a></em>

<h1>Semantic Text Analysis Framework</h1>

<h2>Python</h2>
1. Import framework dependencies: pandas, NLTK, matplotlib.pyplot, sklearn.metrics.ConfusionMatrixDisplay<br>
2. <a href="https://github.com/mtclevans/semantictextanalysis/blob/main/framework/functions.py" target="_blank">Import all required functions</a> for the framework<br>
3. Undertake analysis on the <a href="https://github.com/mtclevans/semantictextanalysis/tree/main/framework/sciercanalysis" target="_blank">Scierc dataset distribution</a><br>
4. Undertaken <a href="https://github.com/mtclevans/semantictextanalysis/tree/main/framework/confusionmatrices" target="_blank">confusion matrix analysis</a> for ner and re<br>
5. <a href="https://github.com/mtclevans/semantictextanalysis/blob/main/framework/posTags.py" target="_blank">Generate POS Tags</a> for Qualitative Data Analysis Software import<br>
6. <a href="https://github.com/mtclevans/semantictextanalysis/blob/main/framework/qdas/dataTransform.py" target="_blank">Transform data and generate .xlsx</a> for Qualitative Data Analysis Software import

<h2>Semantic Text Analysis</h2>
<em>We used Nvivio (REF) on Windows OS.</em><br>
<em>Two users annotated relations to generate a Kappa score.</em><br>
<em>Please note: Not all Nvivo features are present on MacOS:</em><br>
<em>1. Queries will produce different results on Mac OS as they are not filtered by user.</em><br>
<em>2. Cluster Analysis and Pearson’s Correlation Coefficient (WindowsOS only)</em><br>
<em>More information can be found <a href="https://help-nv.qsrinternational.com/20/mac/Content/projects-teamwork/work-with-projects-windows-mac.htm" target="_blank">here</a></em><br><br>.
1. Import exported qdas.xlsx file into Nvivo<br>
2. Undertake Semantic Text Analysis using the <a href="https://github.com/mtclevans/semantictextanalysis/blob/main/framework/codebooks.md" target="_blank">codebooks provided</a><br>
<em>Note: We annotated all themes twice to generate a Kappa statistic.</em>

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
