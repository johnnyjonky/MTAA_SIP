import sipfullproxy
import logging
import socket
import socketserver


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s / %(levelname)s / %(message)s ', filename='proxy.log', level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M:%S')
    sipfullproxy.hostname = socket.gethostname()
    sipfullproxy.ipaddress = socket.gethostbyname(sipfullproxy.hostname)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (sipfullproxy.ipaddress, sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (sipfullproxy.ipaddress, sipfullproxy.PORT)
    print("SIP Proxy server starting at %s:%s on machine %s" % (sipfullproxy.ipaddress, sipfullproxy.PORT, sipfullproxy.hostname))
    server = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()
