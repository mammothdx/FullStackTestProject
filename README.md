# FullStackTestProject

A tiny project with a basic coding exercise. The project includes writing a simple web service using django on sqlite.
The web page will allow the user to run a blast search of a single sequence on a given bacterial genome (in the data folder).
Blast must run using docker!

## Requirements

The following tools are required to complete the task

1) python3 with the following requrements:
```
django
```
2) docker

## Tasks

1) Clone the project into a directory
2) Create a virtual environment
3) Create a webpage that allows the user to enter a single DNA sequence containing only the letter A,G,C and T to a form
4) Use the BlastJob model (models.py) to create the job and run an asychronic search task (use the blast command from the Tools section)
5) A web page should present the job's results when the job if finished

# Tools

Running blast should be done using the `ncbi/blast` image found in ducker hub.
The blast command looks lie this:
`blastn -query <query_file> -subject genome/ecoli_k12_mg1655.fasta -outfmt 6 "<required parameters based on BlastResult model>"`

You can read about the tabular format output 6 [here](http://www.metagenomics.wiki/tools/blast/blastn-output-format-6)