# Benchmark for GPT-Based OncRDS Chatbot
## Thu Oct 24 11:14:57 EDT 2024

This benchmark is designed to evaluate the performance of the OncRDS GPT-based chatbot in answering users' questions accurately and efficiently. The focus is on assessing the chatbot's ability to:

- Provide precise and helpful answers based on OncRDS documentation.
- Clarify technical and biological terms for users with varying levels of expertise.
- Reference appropriate documentation sources or external links when available.
- Respond appropriately when information is unavailable or when questions fall outside the scope of OncRDS.

## Q1.  Please summarize types of data available in OncDRS.
Answer: OncDRS provides a comprehensive and diverse range of clinical data to support healthcare research. These data types are meticulously classified by categories, formats, source systems, and patient demographics, ensuring a rich and robust dataset. Here is a summary of the types of data available in OncDRS:

### 1. Data Categories
- **Diagnosis**
- **Encounters**
- **Health History**
- **Patient Reported Data**
- **Patient Information**
- **Protocols**
- **Test Results**
- **Treatments**

### 2. Data Types 
- **EHR Diagnosis**
- **Outpatient Appointments**
- **Cancer Registry**
- **Clinical Tests**
- **Patient Questionnaires**

### 3. Source Systems
- **DFCI Epic**
- **Historical DFCI IDX**
- **LMR (Longitudinal Medical Record)**
- **RPDR (Research Patient Data Registry)**

### 4. Availability for Adult & Pediatric Populations
Data is categorized into:
- **Adult**
- **Pediatric**
- **Both**

### 5. Patient Inclusion/Exclusion Criteria
Criteria specify which patients are included or excluded from datasets based on factors such as:
- **Timeframes** (e.g., patients seen from 1997 forward)
- **Locations** (e.g., patients treated at DFCI Outpatient clinics)
- **Specific Conditions** (e.g., patients with DFCI Medical Record Numbers)

### Key Features:
- **Data Variety:** Comprehensive inclusion of varied clinical aspects.
- **Source Systems Diversity:** Data from multiple, robust systems.
- **Temporal Range:** Historical and recent data coverage.
- **Age Group Specificity:** Detailed categorization by age groups.
- **Inclusion/Exclusion Criteria Specificity:** Precise patient eligibility criteria for dataset inclusion.

### Conclusion
OncDRS integrates a vast array of clinical data types from numerous source systems, accommodating both adult and pediatric populations, with well-defined inclusion/exclusion criteria, making it a powerful resource for health research.

For more detailed information, you may refer to the following links:
- [OncDRS Data Dictionary Details](https://wiki.dfci.harvard.edu:8443/oncdata/latest/oncdrs-data-dictionary-details)
- [Data Type Summary](https://wiki.dfci.harvard.edu:8443/oncdata/latest/data-type-summary)

## Q2.  What data types are provided by OncDRS?
Answer: OncDRS provides various types of data integrated from different source systems. The data types available include:

1. **Curated Data**: Manually curated and managed by the Population Sciences group, including data for diseases such as Head and Neck, Sarcoma, and Neuro-Oncology. This curated data is institute-funded and does not have a single disease center stewardship.

2. **Imaging Report Data Fields**: This data type includes detailed fields found in imaging reports, which can be highly relevant for analyses involving diagnostic imaging results.

3. **Clinical Text Data**: An overview of clinical text data available within the system, which likely includes unstructured data from clinical notes and other textual records.

4. **Progress Notes Data Fields**: Specific details from progress notes, which are typically used to document ongoing patient care and treatment responses.

5. **Cancer Data**: Details related specifically to cancer patients, including diagnosis codes, staging, and treatment details.

6. **Patient Reported Questionnaire Data**: Data from questionnaires filled out by patients themselves, providing insights into patient-reported outcomes and experiences.

7. **Patient Data**: General patient information which might include demographic details, contact information, and other personal identifiers.

8. **Regimen Data**: Information about treatment regimens, which includes the specifics of chemotherapy or other treatment protocols followed by patients.

These data types are utilized within OncDRS for various purposes such as querying through the Aggregate Query Tool and distribution in detailed Electronic Data Sets. The data provided can be fully identified, limited, or de-identified depending on the user's research requirements and the approval by the user committee and/or DFCI IRB.

For more detailed information, you can refer to:
- [Data Type Summary - OncDRS Data Reference Guide](https://wiki.dfci.harvard.edu:8443/oncdata/latest/data-type-summary)
- [Curated Data Details - OncDRS Data Reference Guide](https://wiki.dfci.harvard.edu:8443/oncdata/latest/oncdrs-data-dictionary-details/curated-data)

## Q3.  Does OncDRS provide CNV data?
Answer: Yes, OncDRS provides Copy Number Variants (CNV) data. This is detailed under the "Copy Number Variants (Genomic_CNV_Results)" section of the OncDRS Data Reference Guide. CNV data includes information on variations in the number of copies of particular regions of the genome, which can be critical in understanding various cancer mechanisms. 

Further details can be found in the OncDRS Data Dictionary:
[Copy Number Variants - Genomic_CNV_Results](https://wiki.dfci.harvard.edu:8443/oncdata/latest/oncdrs-data-dictionary-details/somatic-panel-test-results/copy-number-variants-genomic_cnv_results).

