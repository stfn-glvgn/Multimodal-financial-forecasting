# !/bin/bash

#zip -s0 ACL19_Release.zip --out ACL19_Release_All.zip

#python3 feature_extraction/Financial/generate_price_vol_data.py

#unzip -q ACL19_Release_all.zip
echo "Extracting Text features"
echo "--------"
python3 feature_extraction/Text/text_feature_extraction.py
echo "Done extracting Text features"

#echo "--------"
#echo "Extracting Audio features"
#echo "--------"
#python3 feature_extraction/Audio/audio_feature_extraction.py
#echo "Done extracting Audio features"
#echo "--------"
#echo "Extracting Financial features"
#echo "--------"
#python3 feature_extraction/Financial/finance_feature_extraction.py
#echo "Done extracting Financial features"
#echo "--------"
#echo "Done extracting features!!!"
#echo "--------"