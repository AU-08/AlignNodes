import nuke


def alignNodesRight():
    xpos_ls = []
    for n in nuke.selectedNodes():
        xPos = n.xpos()
        xpos_ls.append(xPos)
    maxPosX = max(xpos_ls)

    # Align on right
    for n in nuke.selectedNodes():
        n.setXpos(maxPosX)

    # Clear the list
    del xpos_ls[:]


def alignNodesLeft():
    xpos_ls = []
    for n in nuke.selectedNodes():
        xPos = n.xpos()
        xpos_ls.append(xPos)
    minPosX = min(xpos_ls)

    # Align on left
    for n in nuke.selectedNodes():
        n.setXpos(minPosX)

    # Clear the list
    del xpos_ls[:]


def alignNodesTop():
    ypos_ls = []
    for n in nuke.selectedNodes():
        yPos = n.ypos()
        ypos_ls.append(yPos)
    minPosY = min(ypos_ls)

    # Align on top
    for n in nuke.selectedNodes():
        n.setYpos(minPosY)

    # Clear the list
    del ypos_ls[:]


def alignNodesBottom():
    ypos_ls = []
    for n in nuke.selectedNodes():
        yPos = n.ypos()
        ypos_ls.append(yPos)

    # SET MINIMUM Y POSITION
    maxPosY = max(ypos_ls)

    # Align
    for n in nuke.selectedNodes():
        n.setYpos(maxPosY)

    # Clear the list
    del ypos_ls[:]


def alignNodesCenter():
    xpos_ls = []
    for n in nuke.selectedNodes():
        xPos = n.xpos()
        xpos_ls.append(xPos)
    maxposX = max(xpos_ls)
    minPosX = min(xpos_ls)
    cenPos = minPosX + ((maxposX - minPosX) / 2)

    # Align
    for n in nuke.selectedNodes():
        n.setXpos(cenPos)

    # List Cleaning
    del xpos_ls[:]
