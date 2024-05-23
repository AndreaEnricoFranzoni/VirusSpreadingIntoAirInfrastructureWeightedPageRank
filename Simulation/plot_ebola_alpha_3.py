import matplotlib.pyplot as plt

ratios = [0.00012132038256856835, 0.0007294108890625582, 0.00423653753116743, 0.021961966432213167, 0.1099140337166462,
          0.41450039075583345, 0.6999776710952328, 0.8480108667336533, 0.923292024859514, 0.9612012950764764,
          0.9800364705444531, 0.9895389081165569, 0.9942555171002195, 0.9966164266309404, 0.9978288861598005,
          0.9984473968218526, 0.9987592571917681, 0.9988969521044992, 0.9989773361616613, 0.9990100852219865,
          0.9990257154553236, 0.999035391314056, 0.9990443228759629, 0.9990450671727885, 0.9990465557664396,
          0.9990465557664396, 0.9990465557664396, 0.9990473000632653, 0.9990473000632653, 0.9990473000632653]

wpr_ratios = [0.00011462171113840199, 0.0006155334747497302, 0.0033173309515834915, 0.016160172676863534,
              0.07167652859960552, 0.29144802947415427, 0.5778727996725094, 0.750339027204049, 0.8391656432585315,
              0.8842045327676678, 0.9066755982285736, 0.9178936399836255, 0.9234639574262216, 0.9262736779427636,
              0.9276737002716683, 0.9283971567861263, 0.9287804696512969, 0.9289464478434, 0.9290305533846898,
              0.9290774440847009, 0.9290997729894682, 0.9291154032228053, 0.9291198690037586, 0.9291213575974099,
              0.9291221018942354, 0.929122846191061, 0.9291235904878866, 0.9291235904878866, 0.9291235904878866,
              0.9291235904878866]

pr_ratios = [0.0001228089762197164, 0.0007442968255740389, 0.004115961445424436, 0.021018198057385286,
             0.09846302705518961, 0.3636552417103941, 0.6403691712254848, 0.7866979271333407, 0.8618272487067843,
             0.8995913810427598, 0.9184749358043988, 0.9279379256447471, 0.9326113654125265, 0.93498864947341,
             0.9361862230657586, 0.9367511443563693, 0.9370496073834245, 0.9372036768263183, 0.9372721521342712,
             0.9373034126009453, 0.9373175542406311, 0.9373257415057125, 0.9373279743961892, 0.9373279743961892,
             0.9373279743961892, 0.9373302072866659, 0.9373302072866659, 0.9373302072866659, 0.9373302072866659,
             0.9373302072866659]

degree_centrality_ratios = [0.00010792303970823564, 0.0006579583938074505, 0.0036150496818131072, 0.017566149380372893,
                            0.07924230583156563, 0.29811990621859996, 0.5761549625990845, 0.753349707863496,
                            0.8443012913549923, 0.8901343455770161, 0.9131606564698002, 0.9246607867217447,
                            0.9304104796993041, 0.9332589036507759, 0.9347147482415987, 0.935446392021138,
                            0.9357954672323322, 0.9359867515165048, 0.9360887201816084, 0.9361423095530498,
                            0.9361728257228983, 0.9361854787689331, 0.9361944103308399, 0.9361958989244911,
                            0.9361966432213167, 0.9361966432213167, 0.9361966432213167, 0.9361966432213167,
                            0.9361966432213167, 0.9361966432213167]
#
random_ratios = [0.00010420155558036545, 0.0006155334747497302, 0.0035852778087901455, 0.019549700420527706,
                 0.09994789922220981, 0.3970689591008894, 0.6851274608313795, 0.840059543746046, 0.9191939265379033,
                 0.9588895091362435, 0.9790071080346843, 0.9889925942465856, 0.9939481225112575, 0.9964124893007331,
                 0.9976822596851624, 0.9982836515202262, 0.9985582970488631, 0.9987116221949314, 0.9987867961743143,
                 0.9988225224219419, 0.998843362733058, 0.9988515499981393, 0.9988567600759183, 0.998858992966395,
                 0.9988604815600461, 0.9988604815600461, 0.9988604815600461, 0.9988604815600461, 0.9988604815600461,
                 0.9988604815600461]

x = range(1, len(ratios) + 1)

_, ax = plt.subplots()

ax.plot(x, ratios, label='No Intervention', color='b', linewidth=1.8)

ax.plot(x, wpr_ratios, label='WPR', color='r')

ax.plot(x, pr_ratios, label='PR', color='m', linewidth=1)
ax.plot(x, degree_centrality_ratios, label='Degree Centrality', color='g')
#
ax.plot(x, random_ratios, label='Random Choice', color='c')

ax.legend()
ax.set_xlabel("Time steps")
ax.set_ylabel("Infection proportion")
plt.grid(True)
plt.savefig('./plot_ebola_alpha_3.png', dpi=300)
plt.show()
