# pylint: disable-msg=C0103

from collections import defaultdict, Counter
import psutil
import operator

conn_list = []
for p in psutil.net_connections(kind='tcp'):
    #Check if laddr, raddr and pid exists
    if  any(p.laddr) and any(p.raddr) and p.pid is not None:
        laddr_var = str(p.laddr)
        laddr_var = laddr_var.replace(',', '@')
        laddr_var = laddr_var.translate(None, "()'' ")
        raddr_var = str(p.raddr)
        raddr_var = raddr_var.replace(',', '@')
        raddr_var = raddr_var.translate(None, "()'' ")
        conn_var = [p.pid, laddr_var, raddr_var, p.status]
        conn_list.append(conn_var)

freq = Counter(item[0] for item in conn_list)
conn_list = sorted(conn_list, key=operator.itemgetter(0))

sorted_list = sorted(conn_list, key=lambda i: freq[i[0]], reverse=True)

print '\"pid\",\"laddr\",\"raddr\",\"status\"'

for field in sorted_list:
    print '"%s","%s","%s","%s"' %(field[0], field[1], field[2], field[3])




