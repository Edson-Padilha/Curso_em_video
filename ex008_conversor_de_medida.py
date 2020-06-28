m = float(input('Digite uma medida em metros: '))
k = m * 0.001
hm = m * 0.01
dam = m * 0.1
dm = m * 10
c = m * 100
mm = m * 1000
print('A medida de {}m ,\n corresponde a, {:.0f} cm \n{:.0f} mm \n{:.0f} dm\n{:.1f} dam\n{:.2f} hm \n{:.3f} km'.format(m,(c),(mm),(dm),(dam),(hm),(k)))