# TADs are 3D structural units of higher-order chromosome organization in Drosophila
## Intoduction

This study utilized Hi-C technology and various advanced tools, including single-cell Hi-C, 3D fluorescent in situ hybridization (FISH), and super-resolution microscopy, to reveal the higher-order chromatin organization. The researchers discovered the significant role of TADs (topologically associating domains) in chromatin folding and confirmed their existence and physical segregation in chromatin through the analysis of FISH data and 3D imaging.

In this final project, we only reproduce the part of Hi-C analysis.


## Members
|Name  | Department   | StudentID     | Cooperation                     |
|----------------|----------|-----------|--------------------------------|
| 黃思穎 Sih-Ying, Huang | Computer Science | 112753110 | Collecting Data, Introduction of paper, Visualization, PPT, Presentation|
| 陳品伃 Pin-Yu, Chen  |  Computer Science | 112753204 |  Collecting Data, Part of Fastq to HiC, Edit Readme, PPT, Presentation |

## Demo 
You might provide an example command or a few commands to reproduce your analysis, i.e., the following R script
```R
Rscript code/your_script.R --input data/training --output results/performance.tsv
```

## Folder organization and its related information
### docs
> Our presentation

  - Click to see [1121_bioinformatics_FP_group2.ppt](https://docs.google.com/presentation/d/1lAboWabTGbrfOJxy_10mEOOY4F6-cIGrbRc8mkmITrI/edit?usp=sharing)

### data
> Original Data - Fastq
  - GES99107 ([NCBI > GEO](https://0-www-ncbi-nlm-nih-gov.brum.beds.ac.uk/geo/query/acc.cgi))
  - Search SRA number ([ENA](https://www.ebi.ac.uk/ena/browser/home))
  - Total size of the original dataset：233.9 GB

| Sample ID |   SRA   |  Label   |  Fastq ID  |   File Size    |
|----------------|----------|---------|-------------|---------------|
| GSM2633507 | SRX2837380 |  S2R+  | SRR5579177_1&2.fastq.gz | 24.5 GB  |
| GSM2633508 | SRX2837381 |  S2R+  | SRR5579178_1&2.fastq.gz | 25.7 GB  |
| GSM2633509 | SRX2837378 |  male  | SRR5579173_1&2.fastq.gz | 13.6 GB  |
| GSM2633509 | SRX2837378 |  male  | SRR5579170_1&2.fastq.gz | 13.7 GB  |
| GSM2633509 | SRX2837378 |  male  | SRR5579171_1&2.fastq.gz | 13.5 GB  |
| GSM2633509 | SRX2837378 |  male  | SRR5579172_1&2.fastq.gz | 13.7 GB  |
| GSM2633510 | SRX2837379 |  male  | SRR5579176_1&2.fastq.gz | 15.4 GB  |
| GSM2633510 | SRX2837379 |  male  | SRR5579174_1&2.fastq.gz | 15.0 GB  |
| GSM2633510 | SRX2837379 |  male  | SRR5579175_1&2.fastq.gz | 14.9 GB  |
| GSM2633511 | SRX2837376 |  ph    | SRR5579166_1&2.fastq.gz | 4.6 GB   |
| GSM2633511 | SRX2837376 |  ph    | SRR5579164_1&2.fastq.gz | 5.0 GB   |
| GSM2633511 | SRX2837376 |  ph    | SRR5579163_1&2.fastq.gz | 4.2 GB   |
| GSM2633511 | SRX2837376 |  ph    | SRR5579161.fastq.gz     | 8.2 GB   |
| GSM2633511 | SRX2837376 |  ph    | SRR5579165_1&2.fastq.gz | 4.9 GB   |
| GSM2633511 | SRX2837376 |  ph    | SRR5579162_1&2.fastq.gz | 4.4 GB   |
| GSM2633511 | SRX2837376 |  ph    | SRR5579160_1&2.fastq.gz | 5.1 GB   |
| GSM2633512 | SRX2837377 |  ph    | SRR5579167_1&2.fastq.gz | 16.8 GB  |
| GSM2633512 | SRX2837377 |  ph    | SRR5579168_1&2.fastq.gz | 15.1 GB  |
| GSM2633512 | SRX2837377 |  ph    | SRR5579169_1&2.fastq.gz | 15.6 GB  |

> Data After Processing

  - **Process pipeline**：fastq -> bam -> pair -> Hi-C
  - Data that we have processed：

| Fastq ID | Original Fastq Size |   BAM Size  |  Pair Size   |  HiC Size   |
|----------------|----------|----------|---------------|---------------|
| SRR5579178 |  25.7 GB  | 26.7 GB | still running |  still running |
    
  Editing....

### code
> Which tools or packages are using in this paper?
  - Hi-C Pro：To do Hi-C data processing and TAD identification
  - Imaris：3D images analysis

> How about us? Which tools or packages we're gonna use?
  - Fanc：Package of python, use ```fanc auto``` to construct a Hi-C Map. And it also can use ```fancplot``` to plot the Hi-C plot.
  - R：Analysis or plot in R studio.

> Data Preprocessing - Fastq to Hi-C
- Build the Environment - Docker
  - **Step1**：Build a DockerFile

    Build a DockerFile with environment, tools, packages that you need to use.
      - We use **ubuntu:latest** to build the environment

  - **Step2**：Pull the Docker Image

    Pull the images which you write in your DockerFile.
    - -t：Tag/Name of the images you pull.
      - This is for MacOS, Linux or Ubuntu. 
    ```bash
    docker build -t <image name>
    ```

      - This is for Windows. 
    ```bash
    docker image build <DockerFile Path> -t <image name>
    ```
  
  - **Step3**：Create a Volume
  
    Create a volume to store your data on Docker.
    ```bash
    docker volume create <volume name>
    ```
  
  - **Step4**：Run the Container

    Data on Docker will be saved under the path "/data".
    ```bash
    docker run --name <container name> -v <volume name>:/data -it <image name>
    ```
  
      - If you already had a container, you can use this command to run it.
    ```bash
    docker start -i <container name or ID>
    ```
  
  > Create shell script and Run on Docker
  - **Step5**：Move the shell script and data to the path on Docker.
  
    Make sure your container is keep running.
    ```bash
    docker cp <local path/file> <container name:/path on docker>
    ```

  - **Step6**：Start to run the shell script
  
    Move your current directory to the path where you store data and shell script, then run sh.
    ```shell
    sh <shell script file>.sh
    ```

  - **Others**：Download dm6 for genome index
    - If you want to use fanc auto to transform fastq to Hi-C, you need to dowload the dm6.fa.gz on this [website](https://hgdownload.soe.ucsc.edu/goldenPath/dm6/bigZips/).

> Visualization

  Editing....

### results
* Which part of the paper do you reproduce?
* Any improvement or change in your package?

## References
### Tools
- Docker 20.10.24 (Environment - Ubuntu:lastest)
- Python 3.10
- R
- Bowtie2

### Python Packages
- fanc 0.9.27
- biopython 1.75

### Related publications
- [Genome reference - dm6](https://hgdownload.soe.ucsc.edu/goldenPath/dm6/bigZips/)
- [Introduction of Hi-C](https://lxz9.com/2021/04/03/HiC/)
