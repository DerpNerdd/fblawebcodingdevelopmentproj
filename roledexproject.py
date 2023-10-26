import random
main_names = [{"id":1,"first_name":"Tamara","last_name":"Dowrey","email":"tdowrey0@dell.com","home_phone":"237-668-3190","cell_phone":"891-212-2704"},
{"id":2,"first_name":"Jodie","last_name":"Bontine","email":"jbontine1@netscape.com","home_phone":"901-787-1070","cell_phone":"731-570-6392"},
{"id":3,"first_name":"Sapphira","last_name":"Whooley","email":"swhooley2@cmu.edu","home_phone":"730-834-2405","cell_phone":"435-241-1924"},
{"id":4,"first_name":"Wallie","last_name":"Nelane","email":"wnelane3@jugem.jp","home_phone":"368-345-7602","cell_phone":"544-826-9484"},
{"id":5,"first_name":"Lauri","last_name":"Edon","email":"ledon4@jugem.jp","home_phone":"439-150-0304","cell_phone":"959-708-6455"},
{"id":6,"first_name":"Elvis","last_name":"Pedrollo","email":"epedrollo5@netscape.com","home_phone":"590-660-4787","cell_phone":"536-122-0951"},
{"id":7,"first_name":"Lisha","last_name":"Askam","email":"laskam6@slideshare.net","home_phone":"886-988-4301","cell_phone":"615-353-2798"},
{"id":8,"first_name":"Mandel","last_name":"Vakhrushev","email":"mvakhrushev7@noaa.gov","home_phone":"155-295-9898","cell_phone":"766-620-6966"},
{"id":9,"first_name":"Bertie","last_name":"Auston","email":"bauston8@about.me","home_phone":"607-611-0071","cell_phone":"982-225-2119"},
{"id":10,"first_name":"Aldin","last_name":"Howgate","email":"ahowgate9@ihg.com","home_phone":"789-763-2167","cell_phone":"754-906-5732"},
{"id":11,"first_name":"Bonnie","last_name":"Snawden","email":"bsnawdena@shinystat.com","home_phone":"498-602-4267","cell_phone":"711-970-4106"},
{"id":12,"first_name":"Rois","last_name":"Passo","email":"rpassob@wired.com","home_phone":"827-321-0384","cell_phone":"381-285-9126"},
{"id":13,"first_name":"Valentine","last_name":"Kemmis","email":"vkemmisc@wisc.edu","home_phone":"611-452-8806","cell_phone":"125-715-5557"},
{"id":14,"first_name":"Crissy","last_name":"Tyrwhitt","email":"ctyrwhittd@berkeley.edu","home_phone":"754-106-2911","cell_phone":"949-144-2346"},
{"id":15,"first_name":"Collin","last_name":"Michelle","email":"cmichellee@xrea.com","home_phone":"616-296-2040","cell_phone":"247-982-4209"},
{"id":16,"first_name":"Dolli","last_name":"Dunderdale","email":"ddunderdalef@opensource.org","home_phone":"792-257-0995","cell_phone":"739-975-1624"},
{"id":17,"first_name":"Jeanette","last_name":"Beavors","email":"jbeavorsg@google.es","home_phone":"380-878-3890","cell_phone":"204-836-0880"},
{"id":18,"first_name":"Vikky","last_name":"Glaum","email":"vglaumh@etsy.com","home_phone":"273-374-8043","cell_phone":"812-583-6715"},
{"id":19,"first_name":"Querida","last_name":"Claussen","email":"qclausseni@sohu.com","home_phone":"583-614-2566","cell_phone":"851-273-5939"},
{"id":20,"first_name":"Lorin","last_name":"Zuenelli","email":"lzuenellij@ebay.co.uk","home_phone":"909-976-7082","cell_phone":"846-922-8549"},
{"id":21,"first_name":"Efren","last_name":"Skilling","email":"eskillingk@globo.com","home_phone":"997-101-1780","cell_phone":"675-238-4609"},
{"id":22,"first_name":"Cross","last_name":"Valintine","email":"cvalintinel@biblegateway.com","home_phone":"177-810-5121","cell_phone":"349-203-6920"},
{"id":23,"first_name":"Ritchie","last_name":"Yellowlea","email":"ryellowleam@microsoft.com","home_phone":"726-890-7478","cell_phone":"459-670-1310"},
{"id":24,"first_name":"Avrom","last_name":"Stode","email":"astoden@jigsy.com","home_phone":"553-904-7540","cell_phone":"164-456-2169"},
{"id":25,"first_name":"Bren","last_name":"Addis","email":"baddiso@wordpress.com","home_phone":"165-599-4604","cell_phone":"759-954-9782"},
{"id":26,"first_name":"Cathi","last_name":"Fountaine","email":"cfountainep@blogtalkradio.com","home_phone":"469-124-8343","cell_phone":"427-562-2704"},
{"id":27,"first_name":"Ayn","last_name":"Linklater","email":"alinklaterq@slate.com","home_phone":"768-767-3753","cell_phone":"811-450-7924"},
{"id":28,"first_name":"Baillie","last_name":"Shah","email":"bshahr@simplemachines.org","home_phone":"793-291-7489","cell_phone":"746-606-5949"},
{"id":29,"first_name":"Lorant","last_name":"Skewis","email":"lskewiss@un.org","home_phone":"336-883-4888","cell_phone":"321-405-9104"},
{"id":30,"first_name":"Daffy","last_name":"Linfoot","email":"dlinfoott@homestead.com","home_phone":"889-111-0185","cell_phone":"474-487-3496"},
{"id":31,"first_name":"Vaughn","last_name":"Burburough","email":"vburburoughu@hp.com","home_phone":"786-775-0617","cell_phone":"902-682-0634"},
{"id":32,"first_name":"Sibeal","last_name":"Stallan","email":"sstallanv@addthis.com","home_phone":"352-295-8735","cell_phone":"385-613-9183"},
{"id":33,"first_name":"Kelsy","last_name":"Tonn","email":"ktonnw@omniture.com","home_phone":"124-461-3393","cell_phone":"376-718-7246"},
{"id":34,"first_name":"Justinian","last_name":"Copcott","email":"jcopcottx@istockphoto.com","home_phone":"977-196-5410","cell_phone":"536-941-3791"},
{"id":35,"first_name":"Abrahan","last_name":"Skillern","email":"askillerny@dedecms.com","home_phone":"949-512-2283","cell_phone":"604-899-3915"},
{"id":36,"first_name":"Ariel","last_name":"MacCorley","email":"amaccorleyz@skype.com","home_phone":"778-915-7504","cell_phone":"261-298-5606"},
{"id":37,"first_name":"Guillaume","last_name":"Crease","email":"gcrease10@indiatimes.com","home_phone":"490-843-2227","cell_phone":"549-454-3757"},
{"id":38,"first_name":"Kenn","last_name":"Ower","email":"kower11@example.com","home_phone":"599-915-1328","cell_phone":"611-370-7763"},
{"id":39,"first_name":"Gerrie","last_name":"Hickinbottom","email":"ghickinbottom12@cam.ac.uk","home_phone":"625-116-4064","cell_phone":"337-220-9199"},
{"id":40,"first_name":"Deina","last_name":"Cromar","email":"dcromar13@mysql.com","home_phone":"823-778-2887","cell_phone":"734-549-0315"},
{"id":41,"first_name":"Greg","last_name":"Ianinotti","email":"gianinotti14@tumblr.com","home_phone":"655-924-3373","cell_phone":"877-595-3651"},
{"id":42,"first_name":"Kailey","last_name":"Sinnocke","email":"ksinnocke15@sphinn.com","home_phone":"858-271-6408","cell_phone":"499-765-3197"},
{"id":43,"first_name":"Petey","last_name":"Kidney","email":"pkidney16@ehow.com","home_phone":"556-284-0278","cell_phone":"645-965-7496"},
{"id":44,"first_name":"Bernadette","last_name":"Dibling","email":"bdibling17@vk.com","home_phone":"139-240-5743","cell_phone":"259-644-1971"},
{"id":45,"first_name":"Sherri","last_name":"Tulk","email":"stulk18@gizmodo.com","home_phone":"837-499-1633","cell_phone":"610-507-9441"},
{"id":46,"first_name":"Nanine","last_name":"Nesbitt","email":"nnesbitt19@trellian.com","home_phone":"918-498-1357","cell_phone":"417-931-1639"},
{"id":47,"first_name":"Finn","last_name":"Honeywood","email":"fhoneywood1a@linkedin.com","home_phone":"906-799-6532","cell_phone":"413-831-7066"},
{"id":48,"first_name":"Yolande","last_name":"Stathers","email":"ystathers1b@plala.or.jp","home_phone":"470-924-3578","cell_phone":"492-753-1695"},
{"id":49,"first_name":"Hewe","last_name":"Lardnar","email":"hlardnar1c@economist.com","home_phone":"276-580-5337","cell_phone":"579-776-4534"},
{"id":50,"first_name":"Wyatan","last_name":"Loisi","email":"wloisi1d@fema.gov","home_phone":"719-343-9899","cell_phone":"694-672-9376"},
{"id":51,"first_name":"Jedidiah","last_name":"Benzi","email":"jbenzi1e@stanford.edu","home_phone":"496-137-4674","cell_phone":"573-831-0890"},
{"id":52,"first_name":"Marvin","last_name":"Mozzini","email":"mmozzini1f@home.pl","home_phone":"772-317-2188","cell_phone":"301-589-5721"},
{"id":53,"first_name":"Bran","last_name":"Shrawley","email":"bshrawley1g@opera.com","home_phone":"416-322-0229","cell_phone":"285-100-0912"},
{"id":54,"first_name":"Bondon","last_name":"Boyton","email":"bboyton1h@multiply.com","home_phone":"349-180-5450","cell_phone":"169-735-9808"},
{"id":55,"first_name":"Skippy","last_name":"Baltzar","email":"sbaltzar1i@google.ru","home_phone":"777-292-9081","cell_phone":"780-961-6724"},
{"id":56,"first_name":"Daniele","last_name":"Marrow","email":"dmarrow1j@redcross.org","home_phone":"749-800-7930","cell_phone":"364-925-1323"},
{"id":57,"first_name":"Shirleen","last_name":"Dohrmann","email":"sdohrmann1k@feedburner.com","home_phone":"481-180-0887","cell_phone":"615-922-0593"},
{"id":58,"first_name":"Eudora","last_name":"Crouse","email":"ecrouse1l@ed.gov","home_phone":"287-296-9077","cell_phone":"303-238-8782"},
{"id":59,"first_name":"Karalynn","last_name":"Meconi","email":"kmeconi1m@eepurl.com","home_phone":"449-225-4657","cell_phone":"877-359-2213"},
{"id":60,"first_name":"Paten","last_name":"Linggood","email":"plinggood1n@acquirethisname.com","home_phone":"501-315-4953","cell_phone":"778-921-5693"},
{"id":61,"first_name":"Nevil","last_name":"Tibbs","email":"ntibbs1o@whitehouse.gov","home_phone":"862-689-0895","cell_phone":"888-936-1197"},
{"id":62,"first_name":"Neill","last_name":"Rickesies","email":"nrickesies1p@apache.org","home_phone":"951-113-8926","cell_phone":"164-635-9020"},
{"id":63,"first_name":"Danice","last_name":"Costelloe","email":"dcostelloe1q@paginegialle.it","home_phone":"868-137-1266","cell_phone":"687-706-0068"},
{"id":64,"first_name":"Torrance","last_name":"Folca","email":"tfolca1r@deliciousdays.com","home_phone":"888-749-5438","cell_phone":"422-880-3498"},
{"id":65,"first_name":"Phaidra","last_name":"Hexham","email":"phexham1s@dot.gov","home_phone":"689-511-2032","cell_phone":"578-292-3413"},
{"id":66,"first_name":"Norina","last_name":"Elgood","email":"nelgood1t@histats.com","home_phone":"629-322-3017","cell_phone":"558-161-3725"},
{"id":67,"first_name":"Raine","last_name":"Cavendish","email":"rcavendish1u@admin.ch","home_phone":"828-690-0665","cell_phone":"784-409-2428"},
{"id":68,"first_name":"Sarge","last_name":"Denekamp","email":"sdenekamp1v@vk.com","home_phone":"447-708-6548","cell_phone":"243-993-2057"},
{"id":69,"first_name":"Lilly","last_name":"Kinforth","email":"lkinforth1w@stumbleupon.com","home_phone":"125-379-7884","cell_phone":"280-734-9785"},
{"id":70,"first_name":"Talya","last_name":"Stooders","email":"tstooders1x@storify.com","home_phone":"556-483-5303","cell_phone":"583-467-8521"},
{"id":71,"first_name":"Yelena","last_name":"Carbett","email":"ycarbett1y@blogtalkradio.com","home_phone":"954-353-6424","cell_phone":"519-928-0797"},
{"id":72,"first_name":"Tomas","last_name":"Shurmore","email":"tshurmore1z@mail.ru","home_phone":"117-729-2241","cell_phone":"268-396-6399"},
{"id":73,"first_name":"Laverne","last_name":"Facchini","email":"lfacchini20@pbs.org","home_phone":"204-238-4244","cell_phone":"405-207-7231"},
{"id":74,"first_name":"Darnall","last_name":"Landers","email":"dlanders21@imgur.com","home_phone":"333-793-6939","cell_phone":"518-636-5491"},
{"id":75,"first_name":"Sherwynd","last_name":"Ottee","email":"sottee22@sphinn.com","home_phone":"343-750-7099","cell_phone":"334-684-7520"},
{"id":76,"first_name":"Thorin","last_name":"Hebditch","email":"thebditch23@msn.com","home_phone":"832-253-5050","cell_phone":"764-865-6114"},
{"id":77,"first_name":"April","last_name":"Goldstein","email":"agoldstein24@fda.gov","home_phone":"309-891-8323","cell_phone":"407-325-0082"},
{"id":78,"first_name":"Sula","last_name":"Hammatt","email":"shammatt25@globo.com","home_phone":"303-208-5699","cell_phone":"942-834-1467"},
{"id":79,"first_name":"Philippa","last_name":"Ellingford","email":"pellingford26@ft.com","home_phone":"638-491-8422","cell_phone":"605-882-0905"},
{"id":80,"first_name":"Annissa","last_name":"Reeder","email":"areeder27@mozilla.org","home_phone":"458-237-2046","cell_phone":"532-928-7840"},
{"id":81,"first_name":"Nydia","last_name":"Pilipets","email":"npilipets28@vkontakte.ru","home_phone":"526-607-9250","cell_phone":"544-854-3831"},
{"id":82,"first_name":"Dasya","last_name":"Drewery","email":"ddrewery29@imdb.com","home_phone":"794-398-7768","cell_phone":"323-306-0811"},
{"id":83,"first_name":"Latrena","last_name":"Oakman","email":"loakman2a@telegraph.co.uk","home_phone":"121-132-6774","cell_phone":"265-710-9704"},
{"id":84,"first_name":"Alvinia","last_name":"Carncross","email":"acarncross2b@twitpic.com","home_phone":"512-500-7406","cell_phone":"942-325-9016"},
{"id":85,"first_name":"Onofredo","last_name":"Springthorp","email":"ospringthorp2c@sakura.ne.jp","home_phone":"361-901-7523","cell_phone":"854-536-0330"},
{"id":86,"first_name":"Evangelia","last_name":"Yurikov","email":"eyurikov2d@gravatar.com","home_phone":"737-239-0769","cell_phone":"127-209-9860"},
{"id":87,"first_name":"Mervin","last_name":"Passie","email":"mpassie2e@spotify.com","home_phone":"729-383-5979","cell_phone":"119-249-2744"},
{"id":88,"first_name":"Clerc","last_name":"Beevors","email":"cbeevors2f@topsy.com","home_phone":"586-304-8669","cell_phone":"240-752-3207"},
{"id":89,"first_name":"Alisa","last_name":"Shower","email":"ashower2g@dailymotion.com","home_phone":"945-919-8162","cell_phone":"437-902-7813"},
{"id":90,"first_name":"Valaria","last_name":"Wakley","email":"vwakley2h@cdc.gov","home_phone":"999-389-3199","cell_phone":"569-901-7192"},
{"id":91,"first_name":"Andrej","last_name":"Leagas","email":"aleagas2i@paginegialle.it","home_phone":"288-362-0049","cell_phone":"111-899-4473"},
{"id":92,"first_name":"Cherise","last_name":"Gauche","email":"cgauche2j@google.com.br","home_phone":"875-595-0586","cell_phone":"174-267-8180"},
{"id":93,"first_name":"Karisa","last_name":"Lewsley","email":"klewsley2k@elegantthemes.com","home_phone":"726-315-0886","cell_phone":"463-513-5060"},
{"id":94,"first_name":"Cass","last_name":"Pagitt","email":"cpagitt2l@fastcompany.com","home_phone":"139-801-3533","cell_phone":"473-614-9110"},
{"id":95,"first_name":"Kirby","last_name":"Hulcoop","email":"khulcoop2m@businessinsider.com","home_phone":"376-863-2639","cell_phone":"979-912-0428"},
{"id":96,"first_name":"Tammi","last_name":"Wolpert","email":"twolpert2n@hp.com","home_phone":"672-554-3093","cell_phone":"206-556-2902"},
{"id":97,"first_name":"Janelle","last_name":"Tzar","email":"jtzar2o@fema.gov","home_phone":"507-624-1862","cell_phone":"259-520-9265"},
{"id":98,"first_name":"Damaris","last_name":"Coal","email":"dcoal2p@networkadvertising.org","home_phone":"278-279-6073","cell_phone":"284-720-6166"},
{"id":99,"first_name":"Rickey","last_name":"Fedder","email":"rfedder2q@com.com","home_phone":"733-634-0950","cell_phone":"373-126-3954"},
{"id":100,"first_name":"Lita","last_name":"Gillman","email":"lgillman2r@washington.edu","home_phone":"382-151-5150","cell_phone":"616-982-7307"},
{"id":101,"first_name":"Atlanta","last_name":"Ebbs","email":"aebbs2s@usnews.com","home_phone":"615-101-4717","cell_phone":"553-414-4289"},
{"id":102,"first_name":"Ahmed","last_name":"Priest","email":"apriest2t@accuweather.com","home_phone":"370-814-2366","cell_phone":"791-688-7635"},
{"id":103,"first_name":"Thomasin","last_name":"Tie","email":"ttie2u@ocn.ne.jp","home_phone":"311-651-8488","cell_phone":"661-136-8496"},
{"id":104,"first_name":"Carmina","last_name":"Carletti","email":"ccarletti2v@cnn.com","home_phone":"609-909-7324","cell_phone":"623-381-1538"},
{"id":105,"first_name":"Shoshanna","last_name":"Doumer","email":"sdoumer2w@washington.edu","home_phone":"624-123-7031","cell_phone":"309-449-7212"},
{"id":106,"first_name":"Kristoffer","last_name":"Adamo","email":"kadamo2x@pcworld.com","home_phone":"865-583-2552","cell_phone":"903-864-9925"},
{"id":107,"first_name":"Colleen","last_name":"Craine","email":"ccraine2y@hud.gov","home_phone":"142-579-3193","cell_phone":"262-375-7373"},
{"id":108,"first_name":"Stanley","last_name":"Krollmann","email":"skrollmann2z@uiuc.edu","home_phone":"406-775-6392","cell_phone":"900-472-9805"},
{"id":109,"first_name":"Guendolen","last_name":"Acum","email":"gacum30@livejournal.com","home_phone":"637-170-9697","cell_phone":"526-898-2747"},
{"id":110,"first_name":"Kaila","last_name":"Cordero","email":"kcordero31@harvard.edu","home_phone":"518-498-3194","cell_phone":"873-608-2033"},
{"id":111,"first_name":"Nerta","last_name":"Servante","email":"nservante32@hostgator.com","home_phone":"958-436-5529","cell_phone":"556-482-6021"},
{"id":112,"first_name":"Harriet","last_name":"Doldon","email":"hdoldon33@irs.gov","home_phone":"297-557-4537","cell_phone":"521-708-1841"},
{"id":113,"first_name":"Stacy","last_name":"Derby","email":"sderby34@lycos.com","home_phone":"611-503-4408","cell_phone":"818-946-9837"},
{"id":114,"first_name":"Hugues","last_name":"Rapier","email":"hrapier35@bizjournals.com","home_phone":"270-518-9378","cell_phone":"575-150-9628"},
{"id":115,"first_name":"Udall","last_name":"Sydry","email":"usydry36@nasa.gov","home_phone":"152-953-5936","cell_phone":"559-744-2211"},
{"id":116,"first_name":"Mitchell","last_name":"Demanche","email":"mdemanche37@github.io","home_phone":"779-527-6032","cell_phone":"354-299-7711"},
{"id":117,"first_name":"Mirna","last_name":"Godthaab","email":"mgodthaab38@nps.gov","home_phone":"294-616-2720","cell_phone":"177-193-0324"},
{"id":118,"first_name":"Lee","last_name":"Ormond","email":"lormond39@sohu.com","home_phone":"756-545-2031","cell_phone":"567-582-4825"},
{"id":119,"first_name":"Inge","last_name":"Abramin","email":"iabramin3a@bing.com","home_phone":"951-186-9828","cell_phone":"456-641-0439"},
{"id":120,"first_name":"Bret","last_name":"Dabbs","email":"bdabbs3b@hud.gov","home_phone":"263-981-8327","cell_phone":"913-816-0701"},
{"id":121,"first_name":"Trista","last_name":"Greer","email":"tgreer3c@sciencedirect.com","home_phone":"734-186-8113","cell_phone":"378-593-3225"},
{"id":122,"first_name":"Hercules","last_name":"Winsiowiecki","email":"hwinsiowiecki3d@simplemachines.org","home_phone":"614-914-5253","cell_phone":"930-654-9326"},
{"id":123,"first_name":"Ingrim","last_name":"Blundel","email":"iblundel3e@typepad.com","home_phone":"938-850-4800","cell_phone":"682-358-5082"},
{"id":124,"first_name":"Alyda","last_name":"Walsom","email":"awalsom3f@timesonline.co.uk","home_phone":"785-265-4090","cell_phone":"543-510-6850"},
{"id":125,"first_name":"Duane","last_name":"Eddington","email":"deddington3g@barnesandnoble.com","home_phone":"428-898-2102","cell_phone":"557-699-7976"},
{"id":126,"first_name":"Rori","last_name":"Benedict","email":"rbenedict3h@spotify.com","home_phone":"383-139-0061","cell_phone":"570-544-8359"},
{"id":127,"first_name":"Darrel","last_name":"Casham","email":"dcasham3i@tinyurl.com","home_phone":"939-137-5135","cell_phone":"502-643-8020"},
{"id":128,"first_name":"Syd","last_name":"Degenhardt","email":"sdegenhardt3j@sun.com","home_phone":"187-125-9537","cell_phone":"900-619-8153"},
{"id":129,"first_name":"Durant","last_name":"Kiddye","email":"dkiddye3k@zimbio.com","home_phone":"752-332-4656","cell_phone":"870-141-3688"},
{"id":130,"first_name":"Atlanta","last_name":"Anfrey","email":"aanfrey3l@nba.com","home_phone":"736-271-0578","cell_phone":"430-509-0951"},
{"id":131,"first_name":"Roland","last_name":"Korb","email":"rkorb3m@meetup.com","home_phone":"437-940-5302","cell_phone":"835-155-1606"},
{"id":132,"first_name":"Cecilius","last_name":"Foxworthy","email":"cfoxworthy3n@mozilla.org","home_phone":"301-607-5978","cell_phone":"284-882-0368"},
{"id":133,"first_name":"Demetris","last_name":"Beminster","email":"dbeminster3o@pen.io","home_phone":"935-240-5680","cell_phone":"297-743-4908"},
{"id":134,"first_name":"Blondell","last_name":"Sibley","email":"bsibley3p@flavors.me","home_phone":"473-258-3718","cell_phone":"721-383-5075"},
{"id":135,"first_name":"Ringo","last_name":"Smout","email":"rsmout3q@privacy.gov.au","home_phone":"480-640-6475","cell_phone":"552-599-7317"},
{"id":136,"first_name":"Ardelle","last_name":"Jacobowitz","email":"ajacobowitz3r@discovery.com","home_phone":"146-916-6890","cell_phone":"759-337-3340"},
{"id":137,"first_name":"Delmore","last_name":"Wife","email":"dwife3s@earthlink.net","home_phone":"364-338-9096","cell_phone":"174-812-9878"},
{"id":138,"first_name":"Nap","last_name":"Lemmanbie","email":"nlemmanbie3t@joomla.org","home_phone":"110-929-8982","cell_phone":"410-163-4440"},
{"id":139,"first_name":"Luciano","last_name":"Aldridge","email":"laldridge3u@ibm.com","home_phone":"277-728-3152","cell_phone":"648-264-1554"},
{"id":140,"first_name":"Ardelia","last_name":"Wilshere","email":"awilshere3v@bbc.co.uk","home_phone":"831-942-2546","cell_phone":"924-419-4392"},
{"id":141,"first_name":"Arlin","last_name":"Kunz","email":"akunz3w@indiegogo.com","home_phone":"920-468-0217","cell_phone":"162-546-2301"},
{"id":142,"first_name":"Prentice","last_name":"Gooderson","email":"pgooderson3x@linkedin.com","home_phone":"632-711-5470","cell_phone":"872-214-9733"},
{"id":143,"first_name":"Anastasia","last_name":"Burgwyn","email":"aburgwyn3y@hp.com","home_phone":"636-333-4392","cell_phone":"892-342-6916"},
{"id":144,"first_name":"Cecil","last_name":"Woodrooffe","email":"cwoodrooffe3z@indiegogo.com","home_phone":"614-687-9001","cell_phone":"339-529-9458"},
{"id":145,"first_name":"Terri","last_name":"Rohlf","email":"trohlf40@myspace.com","home_phone":"842-989-6360","cell_phone":"733-364-9978"},
{"id":146,"first_name":"Faith","last_name":"Morphey","email":"fmorphey41@ucoz.com","home_phone":"758-939-9517","cell_phone":"953-533-5369"},
{"id":147,"first_name":"Ivor","last_name":"Hegel","email":"ihegel42@theglobeandmail.com","home_phone":"679-847-3057","cell_phone":"775-617-6012"},
{"id":148,"first_name":"Gilda","last_name":"Suckling","email":"gsuckling43@discovery.com","home_phone":"449-271-4157","cell_phone":"563-270-4124"},
{"id":149,"first_name":"Elfie","last_name":"Imeson","email":"eimeson44@apache.org","home_phone":"477-168-2097","cell_phone":"769-134-9823"},
{"id":150,"first_name":"Willa","last_name":"Finlry","email":"wfinlry45@hugedomains.com","home_phone":"256-444-6700","cell_phone":"809-436-6873"}]

nicknames = [{"nick_names":"svanhault0"},
{"nick_names":"rshoveller1"},
{"nick_names":"phawler2"},
{"nick_names":"dandren3"},
{"nick_names":"dmacilhargy4"},
{"nick_names":"fsibbert5"},
{"nick_names":"tpindar6"},
{"nick_names":"sduinbleton7"},
{"nick_names":"kjinkins8"},
{"nick_names":"lcalton9"},
{"nick_names":"bcircuitta"},
{"nick_names":"gschimaschkeb"},
{"nick_names":"bjeacockec"},
{"nick_names":"mbrownleed"},
{"nick_names":"abernardeschie"},
{"nick_names":"mpollastrinof"},
{"nick_names":"mdewg"},
{"nick_names":"jtateh"},
{"nick_names":"epawelczyki"},
{"nick_names":"iraschj"},
{"nick_names":"bscoldingk"},
{"nick_names":"mjeanequinl"},
{"nick_names":"hhaslockm"},
{"nick_names":"mhayern"},
{"nick_names":"mbooseyo"},
{"nick_names":"twingeattp"},
{"nick_names":"dvequaudq"},
{"nick_names":"nkixr"},
{"nick_names":"falgars"},
{"nick_names":"gcarot"},
{"nick_names":"hknowlsonu"},
{"nick_names":"tpaynv"},
{"nick_names":"jskacew"},
{"nick_names":"lmartynx"},
{"nick_names":"lcowndeny"},
{"nick_names":"acasterotz"},
{"nick_names":"khail10"},
{"nick_names":"swintle11"},
{"nick_names":"ayurchenko12"},
{"nick_names":"vliddington13"},
{"nick_names":"mmaylour14"},
{"nick_names":"dhaughton15"},
{"nick_names":"jgiblett16"},
{"nick_names":"elawden17"},
{"nick_names":"bfraczak18"},
{"nick_names":"bainger19"},
{"nick_names":"gakister1a"},
{"nick_names":"bprice1b"},
{"nick_names":"abattle1c"},
{"nick_names":"jvalenti1d"},
{"nick_names":"awhitby1e"},
{"nick_names":"hheinsen1f"},
{"nick_names":"bwettern1g"},
{"nick_names":"gsuffe1h"},
{"nick_names":"kmackibbon1i"},
{"nick_names":"kspatoni1j"},
{"nick_names":"kheath1k"},
{"nick_names":"dsalmons1l"},
{"nick_names":"dbeste1m"},
{"nick_names":"abaldinotti1n"},
{"nick_names":"mmatticci1o"},
{"nick_names":"rbowller1p"},
{"nick_names":"blawland1q"},
{"nick_names":"hspowage1r"},
{"nick_names":"fcapenor1s"},
{"nick_names":"dlaetham1t"},
{"nick_names":"pskeleton1u"},
{"nick_names":"jbaldery1v"},
{"nick_names":"ffolkerd1w"},
{"nick_names":"hhamly1x"},
{"nick_names":"pkeenleyside1y"},
{"nick_names":"npoynter1z"},
{"nick_names":"bcossom20"},
{"nick_names":"olartice21"},
{"nick_names":"olevine22"},
{"nick_names":"fpritchard23"},
{"nick_names":"fbeagan24"},
{"nick_names":"tcrawley25"},
{"nick_names":"tjanning26"},
{"nick_names":"vmalamore27"},
{"nick_names":"gteaz28"},
{"nick_names":"maston29"},
{"nick_names":"astonman2a"},
{"nick_names":"jgoodliff2b"},
{"nick_names":"aaleixo2c"},
{"nick_names":"gmarshland2d"},
{"nick_names":"akohnen2e"},
{"nick_names":"dmarland2f"},
{"nick_names":"dferrarello2g"},
{"nick_names":"hleworthy2h"},
{"nick_names":"lchauvey2i"},
{"nick_names":"abeccero2j"},
{"nick_names":"jmacswayde2k"},
{"nick_names":"cfevier2l"},
{"nick_names":"cporter2m"},
{"nick_names":"djayme2n"},
{"nick_names":"ymathiasen2o"},
{"nick_names":"cdufore2p"},
{"nick_names":"nyushin2q"},
{"nick_names":"cmachan2r"},
{"nick_names":"glecount2s"},
{"nick_names":"ldumelow2t"},
{"nick_names":"opolglaze2u"},
{"nick_names":"tpolsin2v"},
{"nick_names":"cmesser2w"},
{"nick_names":"csanto2x"},
{"nick_names":"lbrowett2y"},
{"nick_names":"nangrick2z"},
{"nick_names":"whazart30"},
{"nick_names":"ncousens31"},
{"nick_names":"msarsfield32"},
{"nick_names":"vbrock33"},
{"nick_names":"mdwyr34"},
{"nick_names":"tseeviour35"},
{"nick_names":"zcamerana36"},
{"nick_names":"cabramovicz37"},
{"nick_names":"tmille38"},
{"nick_names":"nfalkous39"},
{"nick_names":"ahardern3a"},
{"nick_names":"lcohr3b"},
{"nick_names":"rkinane3c"},
{"nick_names":"rcappleman3d"},
{"nick_names":"atappington3e"},
{"nick_names":"akarran3f"},
{"nick_names":"spassingham3g"},
{"nick_names":"rdundridge3h"},
{"nick_names":"estandbrooke3i"},
{"nick_names":"aleetham3j"},
{"nick_names":"ewoodward3k"},
{"nick_names":"dkesley3l"},
{"nick_names":"adilland3m"},
{"nick_names":"mcerro3n"},
{"nick_names":"mleatherbarrow3o"},
{"nick_names":"jfreed3p"},
{"nick_names":"ljelf3q"},
{"nick_names":"cbuzzing3r"},
{"nick_names":"mdouch3s"},
{"nick_names":"igrutchfield3t"},
{"nick_names":"ehefforde3u"},
{"nick_names":"lhumbles3v"},
{"nick_names":"rkingsmill3w"},
{"nick_names":"javo3x"},
{"nick_names":"drossoni3y"},
{"nick_names":"idougan3z"},
{"nick_names":"cwinborn40"},
{"nick_names":"efreegard41"},
{"nick_names":"hdorning42"},
{"nick_names":"moxford43"},
{"nick_names":"dcrimpe44"},
{"nick_names":"dbeal45"}]

notes = [
    {"notes": "Person"}, {"notes": "Not a person"}
]

# -----------------------------------------------------------------------------------------------------------------

class Contact:
    def __init__(self, first_name, last_name, home_phone, cell_phone, email, nickname="", notes="", affiliation=""):
        self.first_name = first_name
        self.last_name = last_name
        self.home_phone = home_phone
        self.cell_phone = cell_phone
        self.email = email
        self.nickname = nickname
        self.notes = notes
        self.affiliation = affiliation

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Home Phone: {self.home_phone}, Cell Phone: {self.cell_phone}, Email: {self.email}, Nickname: {self.nickname}, Notes: {self.notes}, Affiliation: {self.affiliation}"
    
# ---------------------------------------------------------------------------------------------------------------
def Sortcontacts(contact):
    return (contact.last_name, contact.first_name)


class Rolodex:
    def __init__(self):
        self.contacts = []

    def Addcontact(self, contact):
        self.contacts.append(contact)

    def Listcontacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"ID: {i}")
                print(contact)

    def Sortcontacts(self):
        self.contacts.sort(key=Sortcontacts)

    def search_contacts(self, search_key, search_value):
        found_contacts = []
        if search_key == "ID":
            try:
                contact_id = int(search_value)
                if 1 <= contact_id <= len(self.contacts):
                    found_contacts.append(self.contacts[contact_id - 1])
            except ValueError:
                pass
        else:
            for contact in self.contacts:
                if getattr(contact, search_key.lower(), None) == search_value:
                    found_contacts.append(contact)
        return found_contacts


# ----------------------------------------------------------------------------------------------
def generate_contact_objects(main_names, affiliations, num_contacts):
    contact_objects = []

    for i in range(num_contacts):
        main_name = main_names[i]
        nickname = random.choice(nicknames)
        note = random.choice(notes)
        contact_affiliation = random.choice(affiliations)

        contact = Contact(
            first_name=main_name["first_name"],
            last_name=main_name["last_name"],
            home_phone=main_name["home_phone"],
            cell_phone=main_name["cell_phone"],
            email=main_name["email"],
            nickname=nickname["nick_names"],
            notes=note["notes"],
            affiliation=contact_affiliation,
        )
        contact_objects.append(contact)

    return contact_objects

# ----------------------------------------------------------------------------------------------


rolodex = Rolodex()

total_contacts = len(main_names)
friend_percentage = 0.30
family_percentage = 0.25
co_worker_percentage = 0.25
acquaintance_percentage = 0.20

num_friends = int(friend_percentage * total_contacts)
num_family = int(family_percentage * total_contacts)
num_co_workers = int(co_worker_percentage * total_contacts)
num_acquaintance = int(acquaintance_percentage * total_contacts)

affiliations = (["Friend"] * num_friends +
               ["Family"] * num_family +
               ["Co-Worker"] * num_co_workers +
               ["Acquaintance"] * num_acquaintance)

random.shuffle(affiliations)

contact_objects = generate_contact_objects(main_names, affiliations, total_contacts)

for contact in contact_objects:
    rolodex.Addcontact(contact)

rolodex.Sortcontacts()

while True:
    print("Options:")
    print("1. List Contacts")
    print("2. Search Contacts")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        rolodex.Listcontacts()
    elif choice == "2":
        search_key = input("Search by (id/first_name/last_name): ").strip().upper()
        search_value = input("Enter the Name or ID #: ").strip()
        found_contacts = rolodex.search_contacts(search_key, search_value)
        if found_contacts:
            print("Matching Contacts:")
            for i, contact in enumerate(found_contacts, start=1):
                print(f"Result {i}:")
                print(contact)
        else:
            print("No matching contacts found.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
