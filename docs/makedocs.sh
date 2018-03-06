#
# makes all yer markdown into html and adds a header and footer.
#

HEADER="doc-parts/header.html"
FOOTER="doc-parts/footer.html"

MARKDOWN_TRANS="kramdown --input GFM 	"
# showdown doesn't do tables properly
# MARKDOWN_TRANS="showdown makehtml --mute -i"

for MD in *.md; do

	BASE="${MD%.*}"
	echo 'Processing' $BASE

	cp $HEADER "$BASE.html"
	$MARKDOWN_TRANS $MD >> "$BASE.html"
	cat $FOOTER >> "$BASE.html"

done
