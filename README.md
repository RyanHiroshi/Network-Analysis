<h1 align="center">
  Network Attack Analysis
</h1>
<p align="center">
<sup>
  <b>Analysing Network Attacks.</b>
</sup>
</p>


## Introduction

The main goal of this program is to show which IP is attacking alot dan which IP is attacked alot to attacks.

To show the data, first we need to acquire the data. in this project, the data is obtained from our lecturer. the data consist of time (in format of UNIX), source IP, Country, latitude, longitude, ASN (Autonomous System Number), destination IP, and source port.

## Data Preparation

The data given is not cleaned and needs to be cleaned in order to be visualized. In order to do that, we use *Pandas* to manipulate our data and dataframes. *Pandas* is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

### Data Cleansing

In consideration to our limited computing power, we decided to split the data in 21 files, each consisting of 1 million entries. We split the data using a simple python script as the following: ![DataSplitter](https://github.com/RyanHiroshi/Network-Analysis/blob/master/Screenshot/Data%20splitter.PNG)  
These files that contain several noise, which does not contribute to our goal, were removed using Microsoft Excel. We sorted out the empty column to get rid of the noise. We managed to found several entries that identifies its 'cntry' column as 'A1' and 'A2' but as described in the ISO 3166 international standard of Alpha-2 Codes, these entries do not match any of them. After successfully cleaning the data, we merged the file back into a file using a simple python script as followed: ![MergeFiles](https://github.com/RyanHiroshi/Network-Analysis/blob/master/Screenshot/Merge%20file.PNG)

### Data Preparation cont.

In consideration to our limited computing power and the enormous size of the data even after cleansing, we decided to prepare our data into: data of network attackers by country, data of network attackers by asn, data of attacker by source ip and frequency, data of attacker after looked up to combined data, data of attacked by dest ip and frequency of being attacked, and data of attacked after looked up to combined data. 

#### Data of network attackers by country

This data is used to provide visualization of which country that has the most network attackers by the frequency of attacks. We decided to plot the data as a choropleth of geographical map using plotly. In order to prepare the data, we used a python script to add Alpha-3 country code because plotly choropleth heatmap cannot understand Alpha-2 code.
![dataCountry](https://github.com/RyanHiroshi/Network-Analysis/blob/master/Screenshot/data%20country.PNG)

#### Data of ASN

This data is used to provide further visualization for other project if needed. We used python script to group the data and dropped some unnecessary columns. ![dataAsn](https://github.com/RyanHiroshi/Network-Analysis/blob/master/Screenshot/data%20asn.PNG)

#### Significant Network Attacker (a)

This data is used to provide visualization of significant network attacker with frequency of attacks >= 10.
![dataAttacker](https://github.com/RyanHiroshi/Network-Analysis/blob/master/Screenshot/data%20attacker.PNG)

### Significant Network being Attacked (b)

This data is used to provide visualization of significant network nodes with frequency of being attacked >= 6
![dataAttacked](https://github.com/RyanHiroshi/Network-Analysis/blob/master/Screenshot/data%20attacked.PNG)

### Looked up data of (a)

This data is used to provide visualization for scatter plot geo map. The data is grouped by source ip and date (by days) and the accumulative value of Frequency.
![lookedupAttacker](https://github.com/RyanHiroshi/Network-Analysis/blob/master/Screenshot/data%20lookedup%20attacker.PNG)


### Looked up data of (b)

This data is used to provide visualization for network graph. Because of the nature of the 'time' data that was in the form of unix timestamp, the data has to be converted into date format.
![lookedupAttacked](https://github.com/RyanHiroshi/Network-Analysis/blob/master/Screenshot/data%20lookedup%20attacked.PNG)

## Visualization with Plotly

The visualization of heatmap has been attached as *heatmap.html*. The python code is as followed: ![heatmap](https://github.com/RyanHiroshi/Network-Analysis/blob/master/Screenshot/heatmap.PNG)

## Visualization With Gephi

The data that has been cleansed is going to be visualized using a network visualization software named Gephi. Gephi is a open-source and free to use. Gephi has functionality to visualize a network.

### Gephi Setup

Gephi can be downloaded free [here](https://gephi.org/users/download/). Gephi is working on a previous version of Java. To be able to run Gephi, you'll have to download and install Java, you can download it [here](https://www.java.com/en/download/). 

After Gephi and Java installed, you need to download the csv import plugin that can be found in Gephi.
This can be done by following the .gif below.

![tutorialPlugin](https://raw.githubusercontent.com/RyanHiroshi/Network-Analysis/master/Screenshot/Installing_Plugin.gif)

after this part you just need to follow the installation.

### About The Datasets

In this visualization step, the data that used here is modified to be able to imported into Gephi. First of all, we gonna have 2 file which have the data for the Nodes and the data for Edges. For the Nodes data the Header should be like the images below.

![nodesHeader](https://raw.githubusercontent.com/RyanHiroshi/Network-Analysis/master/Screenshot/Nodes_Data.PNG)

And for the Edges Data the header should be like the images below.

![edgesHeader](https://raw.githubusercontent.com/RyanHiroshi/Network-Analysis/master/Screenshot/Edges_Data.PNG)

### Importing The Datasets

To import the dataset to the Gephi, first we need to start the Gephi and open a new Project. Then in the Data Labolatory tab, click on "Import Spreadsheet" to open the import window and import your Nodes File. See the .gif below to see the details.

![tutorialImportSpreadsheet](https://raw.githubusercontent.com/RyanHiroshi/Network-Analysis/master/Screenshot/Importing_Spreadsheet.gif)

After that you can choose your Nodes file, and choose the configuration like shown below.

![importNodes](https://raw.githubusercontent.com/RyanHiroshi/Network-Analysis/master/Screenshot/Import_Nodes.PNG)

![importNodes(2)](https://raw.githubusercontent.com/RyanHiroshi/Network-Analysis/master/Screenshot/Import_Nodes(2).PNG)

![importNodes(3)](https://raw.githubusercontent.com/RyanHiroshi/Network-Analysis/master/Screenshot/Import_Nodes(3).PNG)

After Importing the nodes file, then it's time to import the edges file. Importing the edges file is similiar with the nodes file, the crucial part is you need to choose "Append to existing workspace". The details can be seen in the images below.

![importEdges](https://raw.githubusercontent.com/RyanHiroshi/Network-Analysis/master/Screenshot/Import_Edges.PNG)

![importEdges(2)](https://raw.githubusercontent.com/RyanHiroshi/Network-Analysis/master/Screenshot/Import_Edges(2).PNG)

![importEdges(3)](https://raw.githubusercontent.com/RyanHiroshi/Network-Analysis/master/Screenshot/Import_Edges(3).PNG)

### Playing With The Visualization

With Gephi, you can visualize the network data as you like. There is no limit to this, because Gephi has alot of tools and plugin that you can use. Here is some of the experiment that we did.

### Experiment 1

In this experiment, the data that we use is the IP that have been attacked more than 6 times.<br/>
And the configuration used is: <br/>
  -Edges merge strategy that we use is first. <br/>
  -Color is ranked based on In-Degree. <br/>
  -Nodes size is ranked based on In-Degree. <br/>
  -3 Layout used in this experiment is: <br/>
    -Force Atlas 2 with Prevent Overlap ticked. <br/>
    -Fruchterman Reingold with 10x speed. <br/>
    -Noverlap to prevent overlapping edges or nodes. <br/>
    
![experiment1](https://raw.githubusercontent.com/RyanHiroshi/Network-Analysis/master/Screenshot/Experiment_1.PNG)

In this experiment we can conclude that using first as the edges merge strategy doesn't fit this network visualization. It's because using this edges merge strategy doesn't have too much information to be shown than the other edges merge strategy. This edges merge strategy is okay if we just wanted to see the nodes connection.

    
### Experiment 2

In this experiment, the data that we use is the IP that have been attacked more than 6 times.<br/>
And the configuration used is:<br/>
  -Edges merge strategy that we use is Don't Merge.<br/>
  -Color is ranked based on In-Degree.<br/>
  -Nodes size is ranked based on In-Degree.<br/>
  -3 Layout used in this experiment is<br/>
    -Force Atlas 2 with Prevent Overlap ticked.<br/>
    -Fruchterman Reingold with 10x speed.<br/>
    -Noverlap to prevent overlapping edges or nodes.<br/>
    
![experiment2](https://raw.githubusercontent.com/RyanHiroshi/Network-Analysis/master/Screenshot/Experiment_2.PNG)

In this experiment we can conclude that using the Don't merge edges strategy makes the Nodes that have been ranked by In-Degree appears significantly more bigger than the other. We can clearly see the Nodes that have been attacked alot by the size of the nodes.
    
### Experiment 3

In this experiment, the data that we use is the IP that have been attacked more than 6 times.<br/>
And the configuration used is:<br/>
  -Edges merge strategy that we use is SUM.<br/>
  -Color is ranked based on In-Degree.<br/>
  -Nodes size is ranked based on In-Degree.<br/>
  -3 Layout used in this experiment is<br/>
    -Force Atlas 2 with Prevent Overlap ticked.<br/>
    -Fruchterman Reingold with 10x speed.<br/>
    -Noverlap to prevent overlapping edges or nodes.<br/>
    
![experiment3](https://raw.githubusercontent.com/RyanHiroshi/Network-Analysis/master/Screenshot/Experiment_3.PNG)

In this experiment we can see that using SUM as the edges merge strategy makes the edges appears more BOLD. this makes us can see the nodes that are attacking the other IP easily seen.

### Experiment 4

In this experiment, the data that we use is the IP that have been attacked more than 6 times.<br/>
And the configuration used is:<br/>
  -Edges merge strategy that we use is SUM.<br/>
  -Color is ranked based on Out-Degree.<br/>
  -Nodes size is ranked based on Out-Degree.<br/>
  -3 Layout used in this experiment is<br/>
    -Force Atlas 2 with Prevent Overlap ticked.<br/>
    -Fruchterman Reingold with 10x speed.<br/>
    -Noverlap to prevent overlapping edges or nodes.<br/>
    
![experiment4](https://raw.githubusercontent.com/RyanHiroshi/Network-Analysis/master/Screenshot/Experiment_4.PNG)

    
This experiment is specifically made to visualize the Nodes that attacks frequently. Which can be seen with the big Nodes and/or big edges and/or nodes that have darker green means that they are attackers. This is made possible because of the color and nodes is ranked by Out-Degrees and the edges merge strategy is SUM.

## Authors
* **Ryan Hiroshi** - [RyanHiroshi](https://github.com/RyanHiroshi)
* **Albert Antonio** - [mailmancy](https://github.com/mailmancy)

