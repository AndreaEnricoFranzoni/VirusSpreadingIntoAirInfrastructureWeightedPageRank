import matplotlib.pyplot as plt

ratios = [0.005050053961519854, 0.017524468758140746, 0.06030292880800863, 0.1991976480220312, 0.39208291466636896,
          0.5384339994789922, 0.643709575378661, 0.700200960142905, 0.6712083658963195, 0.6085177328718693,
          0.5934196717650999, 0.6064195601205761, 0.6303152097056306, 0.64031111607309, 0.6329031297681516,
          0.6232555543150609, 0.6190889806854973, 0.6213025194447546, 0.6255070522124223, 0.627212980536638,
          0.6258315656283726, 0.6242804510438763, 0.623709575378661, 0.6249577611551487, 0.6253901976108072,
          0.6254341111235161, 0.6250798258345428, 0.6247642439804995, 0.6244940642328161, 0.6241211715232035]

wpr_ratios = [0.0030672472181906144, 0.008332402962301366, 0.025142346767891035, 0.07907483904581147,
              0.2161415652562242, 0.3849242677979978, 0.5134099959063675, 0.6017290015258084, 0.6399307803952217,
              0.6059201369506159, 0.5553116742957092, 0.5450374009154851, 0.559180529195043, 0.5793107811395184,
              0.5857236425886644, 0.5778400506121841, 0.5696840459975439, 0.5672457295969633, 0.5700695917531912,
              0.5744929477875776, 0.5756153474005433, 0.5741408953890812, 0.5715797700122809, 0.5715887015741878,
              0.5719660600647538, 0.5732723009936362, 0.5735030330095642, 0.573767258382643, 0.572952997655465,
              0.5729113170332328]

pr_ratios = [0.002333370548174612, 0.005253246994901567, 0.014454244352647836, 0.04444270775185144, 0.13615868408321238,
             0.32179598824011013, 0.4689196531576793, 0.5752766923449072, 0.6393725577760411, 0.6412839120241152,
             0.5717673328123255, 0.5465423690967958, 0.5537359979159688, 0.5756801012243683, 0.5922987607457855,
             0.5871177105429646, 0.5770004837929367, 0.5711867812883779, 0.5723426742584943, 0.5770027166834133,
             0.5792385843474378, 0.579155967399799, 0.5768650217706821, 0.5752707379703026, 0.5755907856052994,
             0.5762107848610025, 0.5764437497674072, 0.5768947936437051, 0.5761363551784452, 0.5760574597149343]

degree_centrality_ratios = [0.0024033344497785716, 0.005665587436269584, 0.0156622381005545, 0.04792601689553794,
                            0.14603624725540545, 0.33118157121059877, 0.47542034163224295, 0.5796166871348294,
                            0.6408805031446541, 0.6373376502549216, 0.5691660154069443, 0.5463198243459492,
                            0.5547266569908079, 0.5764296081277214, 0.5919422425663354, 0.5855554315060846,
                            0.5763976033642216, 0.5706300472628484, 0.5722555915299021, 0.5773406274422239,
                            0.5797677793904209, 0.5793212012950765, 0.577230471512039, 0.5754240631163708,
                            0.5755230545941722, 0.5764474712515351, 0.5767712403706599, 0.5767243496706487,
                            0.5768441814595661, 0.5764013248483495]

random_ratios = [0.005033679431357225, 0.0176003870343493, 0.0603870343492985, 0.19937404636969222, 0.3918663242901269,
                 0.5390346470172305, 0.6442469576867255, 0.7005991589445871, 0.670971679505787, 0.6085564363067991,
                 0.5931018570205798, 0.6064381675412155, 0.6298902162182278, 0.6399330132856983, 0.6318879088980686,
                 0.6217744036321685, 0.6185635071266421, 0.6217930110528078, 0.626594469874586, 0.6282319228908488,
                 0.6267753340032005, 0.6242216515946559, 0.6234676789103495, 0.6237720963120092, 0.6248007145249526,
                 0.625126716534554, 0.625070894272636, 0.6252986491012615, 0.6249986974805553, 0.6245610509471177]

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
plt.savefig('./plot_big_alpha_2_r.png', dpi=300)
plt.show()