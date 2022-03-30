# Country_in_Classes
Data files are very common in many disciplines. They form the input for a variety of different kinds of processing, analysis, summaries, etc. An associated problem is to maintain these data files – to add information, update or correct information. Manually updating data files can be tedious and can lead to errors. A common approach is to use a program – an update program that takes a data file and a file of updates and then creates a new version of the data file with the updates applied. 


data.txt
Country|Continent|Population|Area
Brazil|South America|193,364,000|8,511,965
Canada|North America|34,207,000|9,976,140
China|Asia|1,339,190,000|9,596,960
Colombia|South America|48,654,392|1,090,909
Egypt|Africa|93,383,574|1,000,000
France|Europe|64,668,129|541,656
Indonesia|Asia|260,581,100|1,809,590
Italy|Europe|59,801,004|300,000
Japan|Asia|127,380,000|377,835
Mexico|North America|128,632,004|1,969,230
Nigeria|Africa|186,987,563|912,134

text_data.txt
Brazil;POP=193,364,111;AREA=8,511,966
Indonesia;POP=260,581,345
Italy;POP=59,801,999
Japan;POP=127,380,555;AREA=377,800
Sweden;POP=9,995,345;AREA=450,295;CON=Europe
Vietnam;AREA=331,310;POP=95,541,921;CON=Asia
Mexico;POP=128,632,777
Colombia;AREA=1,091,111;POP=48,654,404
Egypt;POP=93,384,001
France;POP=64,669,829

upd1.txt
Brazil;POP=193,364,111;AREA=8,511,966
Indonesia;POP=260,581,345
Italy;POP=59,801,999
Japan;POP=127,380,555;AREA=377,800
Sweden;POP=9,995,345;AREA=450,295;CON=Europe
Vietnam;AREA=331,310;POP=95,541,921;CON=Asia
Mexico;POP=128,632,777
Colombia;AREA=1,091,111;POP=48,654,404
Egypt;POP=93,384,001
France;POP=64,669,829
