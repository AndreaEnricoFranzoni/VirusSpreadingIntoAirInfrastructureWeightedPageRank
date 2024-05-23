import matplotlib.pyplot as plt

ratios = [0.0001317405381266049, 0.0002508280302184511, 0.00049570168583231, 0.0009690744668973987,
          0.0019113542480741319, 0.0036872464738937887, 0.007076774217557962, 0.013685385731829853, 0.02603699155223103,
          0.0495470953816382, 0.0921015220870083, 0.1547616389416099, 0.22720330467790556, 0.2917450039075583,
          0.3399918127349187, 0.3658345428156749, 0.36966320568642774, 0.36066167987793535, 0.3548115068289234,
          0.3537508838524804, 0.35495813330356146, 0.3566655502214283, 0.3575512634438614, 0.3570957537866101,
          0.35662461389602174, 0.35661568233411484, 0.3562524654832347, 0.35617580291020057, 0.35627702727847865,
          0.35651817944996467]
wpr_ratios = [0.00011908749209184623, 0.00024338506196271072, 0.000459231141379182, 0.0008425440065498121,
              0.0015533474749730193, 0.0028714971530646423, 0.005197424732983514, 0.009550816865766067,
              0.017312344162852145, 0.03100517286293774, 0.05458747348442559, 0.09524692047188418, 0.1452145435599717,
              0.20552938111718955, 0.2624866956942429, 0.30459975438204756, 0.3263763909046928, 0.33624651110863013,
              0.33244092143947007, 0.32651110863012167, 0.3253812660489003, 0.3261932938856016, 0.3275635443414834,
              0.32842469576867256, 0.3280279855606416, 0.3276178780097503, 0.32743105950653123, 0.3266391276841204,
              0.32647166089836627, 0.3265862826095047]
pr_ratios = [0.00013248483495217892, 0.00026720256038108, 0.0004979345763090321, 0.0009586543113393621,
             0.0018503219083770607, 0.003344869934129731, 0.006028059990324141, 0.010998474191507573,
             0.01974917196978155, 0.03508838524803692, 0.0621874883703621, 0.1065252502698076, 0.16246436678947565,
             0.2256968479029437, 0.2798072271221763, 0.31761899445498865, 0.3349544118194336, 0.3383171448773771,
             0.33101112723754234, 0.32662945182538794, 0.32628335380149603, 0.3281939637527446, 0.32916675970376985,
             0.3300085594134941, 0.3297443340404153, 0.3290283204942131, 0.32856834505600835, 0.32871199434334414,
             0.3284864724051952, 0.32910349447359605]
degree_centrality_ratios = [0.00012876335082430873, 0.00025752670164861746, 0.0004919802017044398,
                            0.0009288824383164006, 0.0017744036321685089, 0.003251088534107402, 0.005897808045848684,
                            0.010760299207323881, 0.01939339808715716, 0.03449071489710096, 0.06080011908749209,
                            0.10537531167429572, 0.16239589148152284, 0.22777194745264412, 0.2817379330877154,
                            0.32015034795876596, 0.3374545048565368, 0.3397908525920137, 0.3307067098358826,
                            0.326926426258792, 0.3267291876000149, 0.32810464813367574, 0.329404190391128,
                            0.329489784526069, 0.32950318186892935, 0.329203230248223, 0.32872241449890216,
                            0.32888839269100517, 0.32932678352126826, 0.32887648394179597]
random_ratios = [0.00013546202225447508, 0.00028134420006698674, 0.0005396151985411782, 0.001013732276431841,
                 0.00199024971158498, 0.0038115440437646534, 0.0072300993636262145, 0.013852108220758438,
                 0.026473149492017418, 0.05004205277064493, 0.09266421048714227, 0.1562613970451416,
                 0.22885117784972647, 0.2929671392951509, 0.34071601354620223, 0.366283353801496, 0.3689509136243534,
                 0.360130996241301, 0.354958877600387, 0.3540024561795244, 0.3553637750734993, 0.35703397715008744,
                 0.3578199545978936, 0.35725577760410854, 0.35731755424063116, 0.3570920323024822, 0.3565993078039522,
                 0.356451192735663, 0.35611104908637564, 0.35591902050537755]

x = range(1, len(ratios) + 1)

_, ax = plt.subplots()

ax.plot(x, ratios, label='No Intervention', color='b', linewidth=1.8)

ax.plot(x, wpr_ratios, label='WPR', color='r')

ax.plot(x, pr_ratios, label='PR', color='m', linewidth=1)
ax.plot(x, degree_centrality_ratios, label='Degree Centrality', color='g')

ax.plot(x, random_ratios, label='Random Choice', color='c')

ax.legend()
ax.set_xlabel("Time steps")
ax.set_ylabel("Infection proportion")

plt.grid(True)
plt.savefig('./plot_arlanda_alpha_1_r.png', dpi=300)
plt.show()
