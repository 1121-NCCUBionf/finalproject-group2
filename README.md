# TADs are 3D structural units of higher-order chromosome organization in Drosophila
## Intoduction

This study utilized Hi-C technology and various advanced tools, including single-cell Hi-C, 3D fluorescent in situ hybridization (FISH), and super-resolution microscopy, to reveal the higher-order chromatin organization. The researchers discovered the significant role of TADs (topologically associating domains) in chromatin folding and confirmed their existence and physical segregation in chromatin through the analysis of FISH data and 3D imaging.

In this final project, we only reproduce the part of Hi-C analysis.


## Members
|Name  | Department   | StudentID     | Cooperation                     |
|----------------|----------|-----------|--------------------------------|
| 黃思穎 Sih-Ying, Huang | Computer Science | 112753110 | Collecting Data   PPT|
| 陳品伃 Pin-Yu, Chen  |  Computer Science | 112753204 |  Editing....            |

## Demo 
You might provide an example command or a few commands to reproduce your analysis, i.e., the following R script
```R
Rscript code/your_script.R --input data/training --output results/performance.tsv
```

## Folder organization and its related information
### docs
> Our presentation

  - Click to see [1121_bioinformatics_FP_group2.ppt](https://docs.google.com/presentation/d/1lAboWabTGbrfOJxy_10mEOOY4F6-cIGrbRc8mkmITrI/edit?usp=sharing)

### data (do not upload fastq file)
* Source
* Format
* Size

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
