
#CRLF = "\n"
CRLF = ""

def add_host(filename, group, hostname, MacAddress, IPAddress, mask, next_server, bootfile):

    with open(filename) as dhcpd_conf:
        dhcpd_lines = dhcpd_conf.readlines()

    prefix = ""
    suffix = ""
    group_bloc = ""
    group_prefix = ""
    group_suffix = ""
    host_bloc = ""

    ret = extract_group_in_group(dhcpd_lines, "group", group)
    prefix = ret[0]
    group_bloc = ret[1]
    suffix = ret[2]

    if group_bloc == "":
        text = "\n\ngroup {\n# " + group + "\n"
        text += "   host " + hostname + " { "
        if MacAddress != "":
            text += "hardware ethernet " + MacAddress + "; "
        if IPAddress != "":
            text += "fixed-address " + IPAddress + "; "
        if mask != "":
            text += "option subnet-mask " + mask + "; "
        if next_server != "":
            text += "next-server " + next_server + "; "
        if bootfile != "":
            text += "filename " + bootfile + "; "
        text += "}\n}\n"
        group_bloc = text
    else:
        ret = extract_group_in_group(group_bloc, "host " + hostname)
        group_prefix = ret[0]
        host_bloc = ret[1]
        group_suffix = ret[2]

        text = "   host " + hostname + " { "
        if MacAddress != "":
            text += "hardware ethernet " + MacAddress + "; "
        if IPAddress != "":
            text += "fixed-address " + IPAddress + "; "
        if mask != "":
            text += "option subnet-mask " + mask + "; "
        if next_server != "":
            text += "next-server " + next_server + "; "
        if bootfile != "":
            text += "filename " + bootfile + "; "
        text += " }\n"

        if host_bloc == "":
            group_prefix = remove_last_brace(group_prefix)
            host_bloc = text
            group_suffix = "}\n"
        else:
            host_bloc = text

        group_bloc = group_prefix + host_bloc + group_suffix

    content = prefix + group_bloc + suffix

    with open(filename, 'w') as f:
        f.write(content)

def extract_group(lines, index):

    i = index
    count_lines = len(lines)

    open_brace = 0
    close_brace = 0

    content = ""

    while i < count_lines and (open_brace != close_brace or open_brace == 0):

        tline = lines[i]
        xline = tline.strip()

        open_brace += xline.count("{")
        close_brace += xline.count("}")

        if len(xline) == 0:
            content += CRLF
        else:
            content += tline + CRLF

            #lt = len(hostname) + 5
            #if xtline[:lt] == "host " + hostname:
            # C'est le host à modifier

            #open_brace += xtline.count("{")
            #close_brace += xtline.count("}")

        i += 1

    #print(content)
    return i-1, content

def extract_group_in_group(lines, keyword, next_keyword = ""):

    part = ["", "", ""]
    part_id = 0
    i = 0
    found = False

    if not isinstance(lines, list):
        CRLF = "\n"
        mlines = lines.split("\n")
    else:
        CRLF = ""
        mlines = lines

    count_lines = len(mlines)

    while i < count_lines:
        dline = mlines[i]
        xline = dline.strip()

        if len(xline) == 0:
            part[part_id] += dline + CRLF
        elif found:
            part[part_id] += dline + CRLF
        #elif xline[0] == "#":
        #    part[part_id] += dline + CRLF
        elif xline[:len(keyword)] == keyword:

            #On se prémunit d'un préfixe de nom identique au nom
            nextChar = xline[len(keyword):len(keyword) + 1]
            if nextChar in [' ', '{', ';', chr(13), chr(10)]:

                if next_keyword == "":
                    part_id = 1
                    ret = extract_group(mlines, i)
                    i = ret[0]
                    part[part_id] = ret[1]
                    part_id = 2
                    found = True
                else:
                    nline = mlines[i+1]
                    nxline = nline.strip()
                    if len(nxline) != 0:
                        if nxline[0] == "#":
                            code = (nxline[1:].strip())[:len(next_keyword)]
                            if code == next_keyword:
                                #C'est notre bloc, il faut l'extraire
                                part_id = 1
                                ret = extract_group(lines, i)
                                i = ret[0]
                                part[part_id] = ret[1]
                                part_id = 2
                                #print("econtent : " + econtent)
                                found = True
                            else:
                                #Ce n'est pas notre bloc ou bloc non identifié, on continue la simple recopie
                                part[part_id] += dline + CRLF
                        else:
                            part[part_id] += dline + CRLF
            else:
                part[part_id] += dline + CRLF
        else:
            part[part_id] += dline + CRLF

        i += 1

    return part

def remove_last_brace(text):

    found = False
    idx = len(text)

    while not found or idx == 0:
        idx -= 1
        if text[idx] == "}":
            text = text[0:idx]
            found = True

    return text

