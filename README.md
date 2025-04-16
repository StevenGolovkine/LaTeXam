# LaTeXam

This project aims to help me generate and correct MCQ.

## Description of the functionalities

1. Load a file that have the questions, the answers and distractors. Which format for this file? JSON? CSV? Other?
2. Create a different LaTeX for each student with a different ordering of the questions/answers. Generate a data matrix barcode to store the specific solutions of each file. The solutions have to be hashed before being encoded as data matrix barcodes. This part can be done in Python.
3. Auto-correct the MCQ by reading an image of the file. Use OCR technology for that. This part can be done in Python / Swift.
4. (Consider making a website to simplify the process.)

### For the functionality 1

The JSON can have the format given in this [file](./examples/sample.json). Once the file is loaded, the questions have to be randomized and after that, the answer and distractors have to be randomized (2 different steps).

### For the functionality 2

The script has to produce two different files, one for the questions and one for the answers. I am going to need two templates: questions_template.tex and answer_template.tex.

### For the functionality 3

The student answer sheets will be collected and scanned. The script should: 
1. Detect the data matrix code.
2. Detect the student name / id.
3. Detect the answer and the uncertainty.
4. Compute the grade.

Loop for each student. Return a file with student name, id and grade.

