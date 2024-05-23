import matplotlib.pyplot as plt

ratios = [0.0002218004540210636, 0.0007733244017714265, 0.0026876558371478547, 0.009472665699080793, 0.032545867291876,
          0.10828700085594135, 0.2657764876632801, 0.4432600200960143, 0.5804562539540769, 0.6842357932343418,
          0.7630233337054817, 0.8220899854862119, 0.866031781474452, 0.8992549588776004, 0.924101075508913,
          0.9427658070038332, 0.9567347698262066, 0.967328346544602, 0.9752618064083957, 0.9812042722637788,
          0.9857072680585017, 0.9890580923672361, 0.9915224591567117, 0.9933772468460422, 0.9947884336273306,
          0.9958624539466339, 0.9966826690484165, 0.9972736407279224, 0.9977135201518366, 0.9980491980201704]

wpr_ratios = [0.00024338506196271072, 0.0007882103382829072, 0.002544750846637639, 0.008268393435301998,
              0.0266026571396673, 0.08354731867068586, 0.19314130475233524, 0.34205425923858435, 0.48419187972163297,
              0.5931614007666257, 0.6755714338878345, 0.7379330877153809, 0.7847084217185814, 0.8198890997729895,
              0.8465267388634587, 0.8660823936585911, 0.8810621115700942, 0.8920099735774627, 0.900260503888951,
              0.9065624651110863, 0.9111674295709129, 0.9146797662907967, 0.917331695880317, 0.9192787763760187,
              0.9207457854192251, 0.9218287373004355, 0.9226407651371367, 0.9232741617357002, 0.923734137173905,
              0.9241003312120873]
pr_ratios = [0.00024487365561385883, 0.0008477540843288303, 0.0028424695768672547, 0.009273194149826951,
             0.02999962785158721, 0.09275873618399018, 0.21688437348814707, 0.3754039671020803, 0.5118402739012318,
             0.6158148189497972, 0.6943239924081723, 0.753279743961892, 0.7970838450374009, 0.8303092553310261,
             0.8552640392988724, 0.8739667299318968, 0.8878285140113877, 0.8983461724535745, 0.9060399687395333,
             0.9118707900710803, 0.9162509768895836, 0.9196762308808752, 0.9222008857132225, 0.9240839566819248,
             0.9255301254140151, 0.9266220088571322, 0.9274154292731942, 0.9279989579844442, 0.9284604220163001,
             0.9288139630084478]
degree_centrality_ratios = [0.00024189646831156264, 0.0007926761192363514, 0.002581221391090767, 0.008403855457556474,
                            0.027177254289010456, 0.0852033791075881, 0.21431133936213762, 0.3855048193219456,
                            0.5195459789363999, 0.6215570689591009, 0.6985069405678985, 0.7560931859625619,
                            0.7996360388522943, 0.8319712701425328, 0.8562122734546537, 0.8743924677161252,
                            0.8880934836812922, 0.8985501097837818, 0.90613300584273, 0.9117650999218488,
                            0.9162346023594209, 0.9195459789363999, 0.9220051356480965, 0.9238100554501135,
                            0.9251334152059841, 0.9261538461538461, 0.9269130289159316, 0.9274757173160656,
                            0.9279267611923635, 0.9282430873432325]
random_ratios = [0.0002218004540210636, 0.000784488854155037, 0.0027635741133564067, 0.009584310222916899,
                 0.033068363663428975, 0.11073722600573109, 0.2744296825574039, 0.4517196978154888, 0.5875181422351233,
                 0.690595809608872, 0.7677920434669346, 0.8260935581109746, 0.869283614305385, 0.9019240072941089,
                 0.9262290201332292, 0.9445335119645715, 0.9581258605932046, 0.9683376130400804, 0.9760031260466674,
                 0.9816724349670649, 0.9859893565553943, 0.9891697368910721, 0.9915909344646645, 0.9933921327825537,
                 0.9947333556622381, 0.9958021659037625, 0.9965985635071266, 0.9971307357374121, 0.9975631721930706,
                 0.9978936399836255]

x = range(1, len(ratios) + 1)

_, ax = plt.subplots()

ax.plot(x, ratios, label='No Intervention', color='b')

ax.plot(x, wpr_ratios, label='WPR', color='r')

ax.plot(x, pr_ratios, label='PR', color='m', linewidth=1.2)
ax.plot(x, degree_centrality_ratios, label='Degree Centrality', color='g')

ax.plot(x, random_ratios, label='Random Choice', color='c', linewidth=1.8)

ax.legend()
ax.set_xlabel("Time steps")
ax.set_ylabel("Infection proportion")
plt.grid(True)
plt.savefig('./plot_arlanda_alpha_2.png', dpi=300)
plt.show()