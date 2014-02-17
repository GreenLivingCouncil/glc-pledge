import pledger
import csv
import sys

def split_name(name):
    tokens = name.split(' ')
    join = lambda l: ' '.join(l)

    if len(tokens) > 2:
        print "How do I split this name?"
        for i in range(1, len(tokens)):
            print "%s) %s, %s" % (i, join(tokens[:i]), join(tokens[i:]))
        while True:
            try:
                split_i = int(raw_input("Choose one: "))
                break
            except KeyboardInterrupt:
                exit(1)
            except:
                pass
    else:
        split_i = 1

    return (join(tokens[:split_i]), join(tokens[split_i:]))

if __name__ == '__main__':
    
    event_id = sys.argv[1]
    pledges = pledger.get_pledges(event_id)
    outfile = open(sys.argv[2], 'wb') \
                if len(sys.argv) > 2 \
                else sys.stdout

    writer = csv.writer(outfile)
    for pledge in pledges:
        first, last = split_name(pledge.name)
        writer.writerow([first, last, pledge.email, pledge.sunetId])

