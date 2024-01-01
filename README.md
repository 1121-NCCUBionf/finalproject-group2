# TADs are 3D structural units of higher-order chromosome organization in Drosophila
## Intoduction


## Members
|Name  | Department   | StudentID     | Cooperation                     |
|----------------|----------|-----------|--------------------------------|
| 黃思穎 Sih-Ying, Huang | Data Science | 112753110 | Editing....                     |
| 陳品伃 Pin-Yu, Chen  |  Data Science | 112753204 |  Editing....            |

## Demo 
### Data Preprocessing - Fatsq to Hic
> Build the Environment - Docker
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

- **Step5**：Start to run the shell script.
```shell
sh <shell script file>.sh
```

### Visualization
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
* Which packages do you use? 
  * original packages in the paper
  * additional packages you found
* Analysis steps

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
