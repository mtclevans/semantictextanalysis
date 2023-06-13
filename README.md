1. Upload pl-marker-evaluation-script folder to Google Drive to upload to model
Note: Upload the entire folder pl-marker-evaluation-script and not just the subfolder pl-marker

2. Open Final_PL_Marker_Evaluation_Script in new notebook file in Google Colaboratory [Folder: pl-marker ipynb file]

3. Change runtime in Google Colaboratory [Runtime -> Change Runtime Type -> GPU -> Save]

4. Run all cells in application. The following steps within step 4 detail the analysis undertaken.
Note: You will need to allow access to your google drive account

4a. Evaluate PL-Marker NER and RE models:
- Import PL-Marker Pre-trained Model by connecting Google Drive
- Installing PL-Marker NER and RE model dependencies
- Evaluate SCINER pretained
- Evaluate SCIRE pretrained

4b. Evaluate SCIERC dataset distribution:
- Data Analysis - Dataset Analysis [Named Entities, Relations, Further Statistics - Sentences]

4c. Analyse confusion matrices:
- Data Analysis - RQ1 - Confusion Matrices [NER]
- Data Analysis - RQ1 - Confusion Matrices [RE]

4d. Generate an .xlsx export for QDAS including POS tags and NER and RE gold labels and predictions:
- Data Analysis - RQ2 - Qdas Data Formatting
- NLTK Default Perceptron POS Tags
- Export to .xlsx file for import to QDAS 

5. Download Qdas.xlsx export from Google Drive pl-marker-evaluation-script/pl-marker/Qdas.xlsx

6. Semantic Text Analysis:
- Open Nvivo Qualitative Data Analysis Software on WindowsOS.

Please note: Not all Nvivo features are present on MacOS:
Queries will produce different results on Mac as they are not filtered by user.
Two users annotated relations to generate a Kappa score.
- Cluster Analysis and Pearson’s Correlation Coefficient (MacOS only)
- Filter queries by user (MacOS only)
For more information see: https://help-nv.qsrinternational.com/20/mac/Content/projects-teamwork/work-with-projects-windows-mac.htm

If annotating SCIERC test set from scratch, import Qdas.xlsx into Nvivo
Else import Nvivo Semantic Text Analysis WindowsOS.nvp [Folder: QDAS - Semantic Text Analysis - RQ2]
- A supplementary MacOS version is provided in the same folder

6a. The SCIERC .xlsx imported annotated dataset is provided under Data -> Files -> SCIERC QDAS Import File - PART-OF & FEATURE-OF

6b. The codebooks are presented in Organize -> Coding -> Codes [For more information please see Appendix E]

6c. Queries are presented in Explore -> Queries -> Query Criteria
Please note: These results will not match the research when running on MacOS.

6d. Query results are presented in Explore -> Queries -> Query Results
Please note: These results will not match the research when running on MacOS.

6e. To generate Pearson’s Correlation Coefficients navigate to:
Explore -> Diagrams -> Cluster Analysis -> Select codes and click ‘next’ -> Select all codes -> Click ‘Finish’ -> Navigate to ‘Summary’ -> Right-click and ‘Export list’
Please note: This feature is not available in MacOS
