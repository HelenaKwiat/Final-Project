#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
from pybaseball.lahman import *

def readFiles():
    global bat2019
    global pitch2019
    global field2019
    bat2019 = pd.read_csv('jupyter/Batting2019.csv', sep = ',', error_bad_lines=False)
    pitch2019 = pd.read_csv('jupyter/Pitching2019.csv', sep = ',', error_bad_lines=False)
    field2019 = pd.read_csv('jupyter/Fielding2019.csv', sep = ',', error_bad_lines=False)
    field2019 = field2019.drop(['Team'], axis = 1)

def getNewStat():
    global newStat
    global batFieldandPitch
    batandField = pd.merge(bat2019, field2019, on ='Name', how = 'outer' )
    batFieldandPitch = pd.merge(batandField, pitch2019, on =['Team', 'Name'], how='outer')
    batFieldandPitch = batFieldandPitch.fillna(0)

    offMin = batFieldandPitch['Off'].min()
    offMax = batFieldandPitch['Off'].max()
    defxMin = batFieldandPitch['Def_x'].min()
    defxMax = batFieldandPitch['Def_x'].max()
    defyMin = batFieldandPitch['Def_y'].min()
    defyMax = batFieldandPitch['Def_y'].max()

    batFieldandPitch['normalize_Off'] = ((batFieldandPitch['Off']-offMin) / (offMax-offMin)) * (10)
    batFieldandPitch['normalize_Def_y'] = ((batFieldandPitch['Def_y']-defyMin) / (defyMax-defyMin)) * (10)
    batFieldandPitch['normalize_Def_y'] = batFieldandPitch['normalize_Def_y'] * -1
    batFieldandPitch['normalize_Def_x'] = ((batFieldandPitch['Def_x']-defxMin) / (defxMax-defxMin)) * (10)
    batFieldandPitch['normalize_Def_x'] = batFieldandPitch['normalize_Def_x'] * -1

    newStat = pd.concat([batFieldandPitch[['normalize_Off', 'Team']].groupby('Team', as_index=False).mean()['Team'], batFieldandPitch[['normalize_Off', 'Team']].groupby('Team', as_index=False).mean()['normalize_Off'] + (batFieldandPitch[['normalize_Def_y', 'Team']].groupby('Team', as_index=False).mean()['normalize_Def_y'] + batFieldandPitch[['normalize_Def_x', 'Team']].groupby('Team', as_index=False).mean()['normalize_Def_x'])/2], axis=1)

    newStat = newStat.drop(newStat.index[[0,1]])
    newStat['teamID'] =  ['LAA', 'HOU', 'OAK', 'TOR', 'ATL', 'MIL', 'STL', 'CHC', 'ARI', 'LAD', 'SFG', 'CLE', 'SEA', 'MIA', 'NYM', 'WSN', 'BAL', 'SDP', 'PHI', 'PIT', 'TEX', 'TBR', 'BOS', 'CIN', 'COL', 'KCR', 'DET', 'MIN', 'CHW', 'NYY']

def combineOtherStats():
    global newStat
    teams = pd.read_csv('core/Teams.csv')
    teams2016 = teams.loc[teams['yearID']==2016]
    teams2016 = teams2016[['teamIDBR', 'W', 'attendance']]
    teams2016['teamID'] = teams2016['teamIDBR']
    newStat = pd.merge(newStat, teams2016, on='teamID')
    salaries = pd.read_csv('core/Salaries.csv')
    salaries = salaries.loc[salaries['yearID'] == 2016]
    salaries = salaries.groupby('teamID', as_index=False).sum()
    salaries = salaries[['teamID', 'salary']]
    newStat = pd.merge(newStat, salaries, on='teamID')


def getValue(value):
    team = newStat.loc[(newStat['teamID']==value)]
    stat = team.iloc[0][0]
    attendance = team.iloc[0]['attendance']
    salary = team.iloc[0]['salary']
    wins = team.iloc[0]['W']

    off = batFieldandPitch.groupby('Team')['Off'].mean()
    print(off)
    # off = off[0].value
    d = batFieldandPitch.groupby('Team')['Def_x'].mean()
    # d = d[0].value
    allStat = newStat[0].to_numpy()
    allAttendance = newStat['attendance'].to_numpy()
    allSalary = newStat['salary'].to_numpy()
    allWins = newStat['W'].to_numpy()

    allStatArray = []
    allAttendanceArray = []
    allSalaryArray = []
    allWinsArray = []
    for i in range(len(allStat)):
        allStatArray.append(allStat[i])
        allAttendanceArray.append(allAttendance[i])
        allSalaryArray.append(allSalary[i])
        allWinsArray.append(allWins[i])

    offArray = []
    defArray = []
    for i in range(len(off)):
        offArray.append(off.iloc[i])
        defArray.append(d.iloc[i])

    data = [stat, attendance, salary, wins, allStatArray, allAttendanceArray, allSalaryArray, allWinsArray, offArray, defArray]

    # print(stat)
    return data

def main():
    readFiles()
    getNewStat()
    combineOtherStats()

main()
