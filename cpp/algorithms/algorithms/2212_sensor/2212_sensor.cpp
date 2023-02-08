//
//  2212_sensor.cpp
//  algorithms
//
//  Created by 정다은 on 2023/02/08.
//
#include <iostream>
#include <stdio.h>
<<<<<<< HEAD
=======
#include <list>
>>>>>>> 09eadfd9944d3980df50e51527d7ac5b0a8cb6fb

using namespace std;

int sub();

int main()
{
    int N, K, data;
    cin >> N >> K;

    list<int> sensors = new list<int>(); 
    list<int>::iterator it = sensors.begin();

    for (int i = 0; i < N; i ++)
    {
        cin >> data; 
        sensors.push_back(data);
    }

    sensors.sort();
    for (it = sensors.begin(); it != sensors.end(); ++it)
    {
        
    }
    
    
}

