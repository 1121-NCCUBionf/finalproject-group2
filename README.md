# TADs are 3D structural units of higher-order chromosome organization in Drosophila
## Intoduction


## Members
|Name  | Department   | StudentID     | Cooperation                     |
|----------------|----------|-----------|--------------------------------|
| 黃思穎 Sih-Ying, Huang | Computer Science | 112753110 | Editing....            |
| 陳品伃 Pin-Yu, Chen  |  Computer Science | 112753204 |  Editing....            |

## Demo 
You might provide an example command or a few commands to reproduce your analysis, i.e., the following R script
```R
Rscript code/your_script.R --input data/training --output results/performance.tsv
```

## Folder organization and its related information
### docs
* Your presentation, 1121_bioinformatics_FP_groupID.ppt/pptx/pdf (i.e.,1121_bioinformatics_FP_group1.ppt), by **01.04**
* Any related document for the project
  * i.e., software user guide

### data (do not upload fastq file)
* Source
* Format
* Size

### code
> Which tools or packages are using in this paper?
  - Hi-C Pro：To do Hi-C data processing and TAD identification
  - Imaris：3D images analysis

> How about us? Which tools or packages we're gonna use?
  - Fanc：Package of python, use ```python fanc auto``` to construct a Hi-C Map. And it also can plot the Hi-C plot.
  - R：Analysis or plot in R studio.

> Data Preprocessing - Fastq to Hic
- Build the Environment - Docker
  - **Step1**：Build a DockerFile

    Build a DockerFile with environment, tools, packages that you need to use.
      - We use **ubuntu:latest** to build the environment

  - **Step2**：Pull the Docker Image

    Pull the images which you write in your DockerFile.
    - -t：Tag/Name of the images you pull.
    ```bash
    docker build -t <image name>
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
    If you want to use fanc auto to transform fastq to Hi-C, you need to dowload the dm6.fa.gz on this [website](https://hgdownload.soe.ucsc.edu/goldenPath/dm6/bigZips/).

> Visualization
  Editing....

### results
* Which part of the paper do you reproduce?
* Any improvement or change in your package?

## References
### Tools
- Docker 20.10.24 (Image - Ubuntu:lastest)
- Python 3.10
- Bowtie2

### Python Packages
- fanc 0.9.27
- biopython 1.75

### Related publications
