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


## Visualization With Gephi

The data that has been cleansed is going to be visualized using a network visualization software named Gephi. Gephi is a open-source and free to use. Gephi has functionality to visualize a network.

### Gephi Setup

Gephi can be downloaded free [here](https://gephi.org/users/download/). Gephi is working on a previous version of Java. To be able to run Gephi, you'll have to download and install Java, you can download it [here](https://www.java.com/en/download/). 

After Gephi and Java installed, you need to download the csv import plugin that can be found in Gephi.
This can be done by following the .gif below.

![tutorialPlugin](https://githubusercontent.com/RyanHiroshi/Network-Analysis/blob/master/Screenshot/Installing_Plugin.gif)

### About The Datasets

In this visualization step, the data that used here is modified to be able to imported into Gephi.
