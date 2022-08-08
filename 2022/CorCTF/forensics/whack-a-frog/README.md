# whack-a-frog
## Description
Come play a game of Whack-a-Frog **here** and let all your anger out on the silly msfrogs. Due to lawsuits by Murdoch, we were forced to add DRM protection, which has allowed us to detect a player distributing copyrighted media. Thankfully, we took a pcap: can you make out what he was sharing? Make sure that anything you find is all typed in UPPERCASE and is wrapped like corctf{text}. Best of luck and enjoy whacking some frogs!
 
Links: https://whack-a-frog.be.ax/
Files: whacking-the-froggers.pcap

## Solution
First thought that came to mind when seeing the file name is that I have to use Wireshark to analyze the .pcap file.

Going to the website linked above, we're greeted with a nice 'frog-matrix' that we can... Hammer frogs into wells?... For some reason?... 
<img width="1278" alt="SiteView" src="https://user-images.githubusercontent.com/63298621/183505965-f785ac5a-e57e-4f8f-ae4f-06f17837d86a.png">
(Not asking questions of people's frustrations. So we will skip over that.)

Anyway the description also really sells the idea that we have to 'make out what he was sharing' possibly using the site shown. 
If we inspect the site and check the Network tab we can see there was some kind of fetch operation whenever we move the mouse cursor on the site.
<img width="1278" alt="SiteInspect" src="https://user-images.githubusercontent.com/63298621/183505961-7955fd2a-2d80-4abb-b4cf-682cbdb2a12b.png">

And sure enough, our mouse coordinates are logged by the anticheat system.
<img width="733" alt="Anticheat" src="https://user-images.githubusercontent.com/63298621/183505925-68eb0274-bfca-4761-875e-8a4476bdf012.png">

Checking the page source gives us no leads, so what it seems like is using the Network records of the .pcap file we have to figure out what was 'drawn' on the website frog-matrix. Okay. Great.

Opening up the .pcap using Wireshark we are greeted with a boatload of information on network activity.

<img width="1280" alt="pcapopen" src="https://user-images.githubusercontent.com/63298621/183505941-e8f5c193-da78-41e1-95bc-2232dd9f77de.png">

But we are only concerned about the mouse coordinates, so we flip through some of the rows and find that HTTP types have the 'anticheat' tag that we have seen earlier. 
Something like 'GET /anticheat?x=365&y=10&event=mousemove HTTP/1.1\r\n" will be seen.

Sweet, now we filter out only those information. So that's easily done on Wireshark by filtering by 'http contains GET'. 

<img width="1280" alt="pcapsorted" src="https://user-images.githubusercontent.com/63298621/183505947-a46c1634-ff61-4571-846d-d1e12c0d1576.png">

How do we extract out the information from the 'Info' field? Well, digging some more tells us we can use 'tshark' to do just that. So we install tshark and do a little but more digging to figure out how to extract out just the info fields after we have filtered the pcap file.

tshark -r whacking-the-froggers.pcap -Y "http contains GET" -e _ws.col.Info -T fields > stripped.txt

More information on this can be found in the tshark documentation if you're interested.

Now we have a file containing all the sweet sweet mouse coords. Yum. 

<img width="362" alt="coords" src="https://user-images.githubusercontent.com/63298621/183505933-d7098898-10b6-44b4-8f7d-57c1179b1988.png">

But we're still not done. We just need the x=*** y=*** coordinates. So we can do that by running a **python** or using **sed/gawk/grep**. I used **grep, tr and sed** by looking up different sites on how to use them to get all the coordinates in the format "-365 -10". 

cat stripped.txt | grep -oE '[0-9]+&y=[0-9]+' | tr -d '&y' > coords2.txt
This uses grep to get the numbers in this format '365&y=10' but that's not workable, so use tr alongside to delete the '&y' characters.
Now our coords2.txt file contents looks like this:

<img width="482" alt="coordswequal" src="https://user-images.githubusercontent.com/63298621/183505939-455f0c9d-c4ef-479c-9c35-7bb2b3c38dfe.png">

sed -i 's/=/ -/g' coords2.txt 
A bit clumsy but I use sed to replace the '=' characters with ' -'.

sed -i 's/^/-/' coords2.txt_
And add a '-' character to the beginning of each line.

<img width="494" alt="coordsformatted" src="https://user-images.githubusercontent.com/63298621/183505937-a72fbbe6-fc41-4796-9f0f-831d73eef70a.png">

Now my file is now looking all nice and sorted.

Now using **gluplot** to graph the coordinates should give us whatever was recorded of the mouse movement.
gnuplot
plot 'coords2.txt'
<
img width="541" alt="commandstoformat" src="https://user-images.githubusercontent.com/63298621/183505930-0b538488-5fa2-4e56-8c2f-b07b567aa1c8.png">

This is our output:

<img width="494" alt="plot" src="https://user-images.githubusercontent.com/63298621/183505953-1b8ce1c8-6e74-4952-97da-a53e9ad491ca.png">

Looks promising, and observing for a but tells us we need to mirror the graph, that can be done easily.

<img width="602" alt="flipped" src="https://user-images.githubusercontent.com/63298621/183507663-77ae3dd0-371f-4b6c-88ef-0329bd4ec1f6.png">

Plot shows **LILYXOX**.

SO according to the description we can conclude that the flag will be 'corctf{LILYXOX}'.

### **flag :** corctf{LILYXOX}
