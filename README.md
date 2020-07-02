# gw_style
A Gordon Walters' koru style filter

This program is inspired by [The Koru series](http://www.art-newzealand.com/Issues1to40/walters.htm) of [Gordon Walters](https://en.wikipedia.org/wiki/Gordon_Walters). It can create a random koru style image or can be used as an image/video filter.

The koru image is generated base on a low resolution image in grayscale. White pixels are used for representing circles. Also, the white pixels are checked and deleted to keep a suitable distance. So that the circles will not overlap eachother.

The basic generator method can create two random lines in grayscale image to simulate the painting on the [poster](https://www.aucklandartgallery.com/whats-on/exhibition/gordon-walters-new-vision).

<table>
<tr>
<td><img src="https://rfacdn.nz/artgallery/assets/media/2018-gordon-walters-new-vision-mobile-5.jpg" width="500px"></td>
<td><img src="https://github.com/ZZ76/gw_style/blob/master/samples/gwp.png" width="500px"></td>
<td><img src="https://github.com/ZZ76/gw_style/blob/master/bnr2.png" width="100px"></td>
</tr>
<tr>
<td>Poster from Auckland art gallery</td>
<td>Generated image based on binary image</td>
<td>The binary image</td>
</tr>
</table>

Also, the program can transfer a given grayscale image into koru style.

<table>
<tr>
<td><img src="http://www.artnet.com/WebServices/images/ll00008lldRtMJFgJ7bR3CfDrCWvaHBOc7M6E/gordon-walters-arahura.jpg" width="500px"></td>
<td><img src="https://github.com/ZZ76/gw_style/blob/master/samples/gwa.png" width="500px"></td>
<td><img src="https://github.com/ZZ76/gw_style/blob/master/bnr1.png" width="100px"></td>
</tr>
<tr>
<td><a href="http://www.artnet.com/artists/gordon-walters/arahura-hFBZT0kFDPAU28-76ocXJg2">Arahura by Gordon Walters</a></td>
<td>The fake one which looks satisfying</td>
<td>The binary image is drawn manually</td>
</tr>
</table>

For a general image or video, they will be converted into grayscale at first.

<table>
<tr>
<td><img src="https://github.com/ZZ76/gw_style/blob/master/samples/ori.png" width="500px"></td>
<td><img src="https://github.com/ZZ76/gw_style/blob/master/samples/main.png" width="500px"></td>
</tr>
<tr>
<td><img src="https://github.com/ZZ76/gw_style/blob/master/samples/lrg.png" width="500px"></td>
<td><img src="https://github.com/ZZ76/gw_style/blob/master/samples/lrg2.png" width="500px"></td>
</tr>
</table>

More intresting results

![](/samples/legoface.png)
</br>
![](/samples/king.png)
