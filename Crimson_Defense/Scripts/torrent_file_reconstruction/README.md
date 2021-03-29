# Torrent files
You can use this if you have a pcap file containing a torrent file and you want to put it back together</br>
To get the pieces you need to follow the stream and get a hex</br>

to get the count export the pieces to a text file and use the countTorrentPieces script</br>  

To reconstruct use this tshark command in the command line and copy and paste it into a text file</br>
Use the readTorrentPieces to read every piece into a construct file</br>
tshark -r torrent.pcap -Y 'bittorrent.piece.data and ip.dst_host == 192.168.29.129' -T fields -e frame.number -e frame.time -e frame.len -e ip.src_host -e bittorrent.piece.index -e bittorrent.piece.data -E separator=+</br>

This command will give some good details on the torrent file. Frames count IS NOT the same as the number of pieces. There can be multiple pieces in a frame.</br> 
tshark -r torrent.pcap -q -z io,stat,1,"bittorrent.piece.data and ip.dst_host == 192.168.29.129"</br>

Finally use the constructTorrentPieces to reconstuct the torrent file.</br>