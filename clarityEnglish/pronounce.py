from bs4 import BeautifulSoup
content = '''


               <li id="e0xxjmjeJMDIQXvXnXfy_mA">
              <button class="audio-recorder-button mod-marked" data-audio-recorder-src="https://content.clarityenglish.com/cp/media/audio/namen/CP_Aud_C02U08E05_15.mp3" data-length="2" data-auto-stop=""></button>
              <p>
                <span class="tab-space">
                  <span class="highlight tab-xlarge mod-phonemic-script">/seɪvd/</span>
                  <input id="etqhE5M1GOKDLcCBMaml3TQ" class="gapfill mod-neutral" style="width: 65px;" autocapitalize="none" spellcheck="false" autocomplete="off" data_last_value=""><span id="marking-25dca409-7686-458c-8911-32a5ad89cdd9" class="js-after-select mod-neutral"></span>
                </span>
              </p>
            </li>
<li id="eNGiLBciEnJwjL0GjCV-sUg">
              <button class="audio-recorder-button mod-marked" data-audio-recorder-src="https://content.clarityenglish.com/cp/media/audio/namen/CP_Aud_C02U08E05_16.mp3" data-length="2" data-auto-stop=""></button>
              <p>
                <span class="tab-space">
                  <span class="highlight tab-xlarge mod-phonemic-script">/bʌs/</span>
                  <input id="eHeinR4Y4k4M1anQIjz4xig" class="gapfill mod-neutral" style="width: 47px;" autocapitalize="none" spellcheck="false" autocomplete="off" data_last_value=""><span id="marking-f7a490b2-0d40-4af8-ad70-077377011b31" class="js-after-select mod-neutral"></span>
                </span>
              </p>
            </li>
<li id="eiGb2EGMeip_UzoZ4cIykmw">
              <button class="audio-recorder-button mod-marked" data-audio-recorder-src="https://content.clarityenglish.com/cp/media/audio/namen/CP_Aud_C02U08E05_11.mp3" data-length="2" data-auto-stop=""></button>
              <p>
                <span class="tab-space">
                  <span class="highlight tab-xlarge mod-phonemic-script">/ˈsʌniː/</span>
                  <input id="ebDphnZ9tbyj8CM_f1viaRA" class="gapfill mod-neutral" style="width: 65px;" autocapitalize="none" spellcheck="false" autocomplete="off" data_last_value=""><span id="marking-5f078a69-7cdd-406b-b3fe-b25eff3b40da" class="js-after-select mod-neutral"></span>
                </span>
              </p>
            </li>
<li id="eLKkeSosvNbcddAqqAbg96w">
              <button class="audio-recorder-button mod-marked" data-audio-recorder-src="https://content.clarityenglish.com/cp/media/audio/namen/CP_Aud_C02U08E05_1.mp3" data-length="2" data-auto-stop=""></button>
              <p>
                <span class="tab-space">
                  <span class="highlight tab-xlarge mod-phonemic-script">/θriː/</span>
                  <input id="eD-BuN0BuFRMqAbbX0qG80Q" class="gapfill mod-neutral" style="width: 60px;" autocapitalize="none" spellcheck="false" autocomplete="off" data_last_value=""><span id="marking-006e4bf8-4bdb-4bb7-9e10-3b45e39cebcd" class="js-after-select mod-neutral"></span>
                </span>
              </p>
            </li>
<li id="eBx1wROiETD4IvvIlaXJCVw">
              <button class="audio-recorder-button mod-marked" data-audio-recorder-src="https://content.clarityenglish.com/cp/media/audio/namen/CP_Aud_C02U08E05_9.mp3" data-length="2" data-auto-stop=""></button>
              <p>
                <span class="tab-space">
				  <span class="highlight tab-xlarge mod-phonemic-script">/ˈbɜːrθdeɪ/</span>
                  <input id="ePrcNYMMfJjcO989e6Xoz_A" class="gapfill mod-neutral" style="width: 83px;" autocapitalize="none" spellcheck="false" autocomplete="off" data_last_value=""><span id="marking-22f091af-7c1a-4492-b0d1-5f6d7f46dd43" class="js-after-select mod-neutral"></span>
                </span>
              </p>
            </li>
<li id="e_x_h-bQpH7Cge1IONSxceg">
              <button class="audio-recorder-button mod-marked" data-audio-recorder-src="https://content.clarityenglish.com/cp/media/audio/namen/CP_Aud_C02U08E05_8.mp3" data-length="2" data-auto-stop=""></button>
              <p>
                <span class="tab-space">
                  <span class="highlight tab-xlarge mod-phonemic-script">/wɜːrθ/</span>
                  <input id="etSPfzpXWNxca1-NMAQ31uQ" class="gapfill mod-neutral" style="width: 62px;" autocapitalize="none" spellcheck="false" autocomplete="off" data_last_value=""><span id="marking-c956a533-1d25-4e5f-8065-f41ffb37d645" class="js-after-select mod-neutral"></span>
                </span>
              </p>
            </li>
<li id="eggaAm95GI6HuZUsXx_hjcA">
              <button class="audio-recorder-button mod-marked" data-audio-recorder-src="https://content.clarityenglish.com/cp/media/audio/namen/CP_Aud_C02U08E05_7.mp3" data-length="2" data-auto-stop=""></button>
              <p>
                <span class="tab-space">
                  <span class="highlight tab-xlarge mod-phonemic-script">/θæŋks/</span>
                  <input id="eLFuhItmKyt0qf5c6zi8bXA" class="gapfill mod-neutral" style="width: 68px;" autocapitalize="none" spellcheck="false" autocomplete="off" data_last_value=""><span id="marking-b28024e0-5aad-49bf-bc67-dde46ecde55f" class="js-after-select mod-neutral"></span>
                </span>
              </p>
            </li>
<li id="eG7nfEB6d-KB-z0wrf5tTNw">
              <button class="audio-recorder-button mod-marked" data-audio-recorder-src="https://content.clarityenglish.com/cp/media/audio/namen/CP_Aud_C02U08E05_2.mp3" data-length="2" data-auto-stop=""></button>
              <p>
                <span class="tab-space">
                  <span class="highlight tab-xlarge mod-phonemic-script">/ˈsʌmθɪŋ/</span>
                  <input id="evYbX94PnzivNj0C4omljbg" class="gapfill mod-neutral" style="width: 102px;" autocapitalize="none" spellcheck="false" autocomplete="off" data_last_value=""><span id="marking-b162b757-d9ed-4988-ab1b-21d54a12c5ae" class="js-after-select mod-neutral"></span>
                </span>
              </p>
            </li>
<li id="e6r5WySL5MVF55TolwsY8vA">
              <button class="audio-recorder-button mod-marked" data-audio-recorder-src="https://content.clarityenglish.com/cp/media/audio/namen/CP_Aud_C02U08E05_19.mp3" data-length="2" data-auto-stop=""></button>
              <p>
                <span class="tab-space">
				  <span class="highlight tab-xlarge mod-phonemic-script">/ˈæskɪŋ/</span>
                  <input id="eLdi-_eGlYiCob0Rn_ib7RQ" class="gapfill mod-neutral" style="width: 68px;" autocapitalize="none" spellcheck="false" autocomplete="off" data_last_value=""><span id="marking-a2b85b41-d824-4e00-a9e6-9bf41c30e745" class="js-after-select mod-neutral"></span>
                </span>
              </p>
            </li>
<li id="e6PCkXPu_j2vo0NmIlD6sYw">
              <button class="audio-recorder-button mod-marked" data-audio-recorder-src="https://content.clarityenglish.com/cp/media/audio/namen/CP_Aud_C02U08E05_10.mp3" data-length="2" data-auto-stop=""></button>
              <p>
                <span class="tab-space">
                  <span class="highlight tab-xlarge mod-phonemic-script">/maʊθ/</span>
                  <input id="et7THAlzVNCBYHvOXdhuBrw" class="gapfill mod-neutral" style="width: 70px;" autocapitalize="none" spellcheck="false" autocomplete="off" data_last_value=""><span id="marking-bfeed3a9-2619-4bab-bc61-256eab214632" class="js-after-select mod-neutral"></span>
                </span>
              </p>
            </li> 
            
            
'''


soup = BeautifulSoup(content)

person = {}

# print(soup)

answers = soup.find_all(class_='highlight')
# print(type(answers))

text = []

for answer in answers:
    x = str(answer).split('/')
    text.append(x[1])

for i in text:
    print(i)
