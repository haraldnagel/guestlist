# guestlist

Quick hack Python script to work with dnsmasq for keeping track of who is getting IP addresses on the network.

## Setup

1. Run `gl-maketable.py` to make the SQLite database (`guestlist.db`).
2. Modify dnsmasq configuration to call `gl.py`, sample config file snippet:

```
# Run an executable when a DHCP lease is created or destroyed.
# The arguments sent to the script are "add" or "del",
# then the MAC address, the IP address and finally the hostname
# if there is one.
#dhcp-script=/bin/echo
dhcp-script=/guestlist/gl.py
```

3. View the results with `./gl-print.py`.

## License

This code is released under the [MIT License](https://github.com/haraldnagel/guestlist/blob/master/LICENSE).

