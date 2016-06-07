#!/usr/bin/python

def read_sensor(readouts,sensor,interval):
    import time
    from time import gmtime, strftime
    import grovepi

    while readouts > 0:
        try:
            print("{}, {}".format(strftime("%d-%m-%Y, %H:%M:%S", gmtime()), grovepi.analogRead(sensor)))
            time.sleep(interval)
            readouts=readouts-1
        except KeyboardInterrupt:
            break
        except IOError:
            print ("Error")

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Read moisture Sensor')
    parser.add_argument('-s', '--sensor',
                    dest='sensor',
                    action='store',
                    default='0',
                    type=int,
                    metavar='<int>',
                    help='Set sensor to read out. Default is: [%(default)s]')
    parser.add_argument('-i', '--interval',
                    dest='interval',
                    action='store',
                    default='5',
                    type=int,
                    metavar='<int>',
                    help='Set readout interval. Default is: [%(default)s]')
    parser.add_argument('-r', '--readouts',
                    dest='readouts',
                    action='store',
                    default='5',
                    type=int,
                    metavar='<int>',
                    help='Specify how many readouts you want. Default is: [%(default)s]')
    args = parser.parse_args()

    read_sensor(args.readouts,args.sensor,args.interval)


if __name__=='__main__':
    main()
