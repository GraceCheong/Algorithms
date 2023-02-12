//
//  2212_sensor.cpp
//  algorithms
//
//  Created by 정다은 on 2023/02/08.
//
#include <iostream>
#include <stdio.h>
#include <list>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

struct mNode
{
    int left = 0;
    int right = 0;
};

int installrecv(int s, int e, int& k, map<int, mNode>& diff, vector<int>& sensors);


int main()
{
    int N, input;
    int K = 0;
    
    cin >> N >> K;
    if (K >= N)
    {
//        cout << 0 << endl;
        return 0;
    }
    map<int, mNode>* diff = new map<int, mNode>;
    vector<int>* sensors = new vector<int>;
    
    
    for (int i = 0; i < N; i ++)
    {
        cin >> input;
        sensors->push_back(input);
    }
    sort(sensors->begin(), sensors->end());
    sensors->erase(unique(sensors->begin(), sensors->end()), sensors->end());
    
    
    
    map<int, mNode>::iterator now = diff->begin();
    vector<int>::iterator it;

    int nData = 0, pData = 0;

    for (it = sensors->begin(); it != sensors->end(); ++it)
    {
        nData = *it;
        
        if (it == sensors->begin())
        {
            pData = nData;
            continue;
        }
        int d = nData - pData;
        
        (*diff)[pData].right = d;
        (*diff)[nData].left = d;
        
        pData = nData;
        
    }
//
//    cout << "size of sensors : " << sensors->size() << endl;
//    cout << "size of diff : " << diff->size() << endl;
    int size = sensors->size();
    
    cout << installrecv(0, size-1, K, *diff, *sensors) << endl;
    
    return 0;
}

int installrecv(int s, int e, int& k, map<int, mNode>& diff, vector<int>& sensors)
{
    // 더이상 남은 갯수가 없으면, 거리 총합 구하귀
    //
    if (e < s)
    {
        return 0;
    }
    
    if (k <= 0)
    {
        int total = 0;
        if (e > s)
        {
            for(int i = s; i < e; i++)
            {
                total += diff[sensors[i]].right;
            }
        }
        
        if (diff[sensors[s]].left == 0)
        {
            total += diff[sensors[e]].right;
        }
        else if (diff[sensors[e]].right == 0 )
        {
            total += diff[sensors[s]].left;
        }
        else if(diff[sensors[e]].right < diff[sensors[s]].left)
        {
            total += diff[sensors[e]].right;
        }
        else
        {
            total += diff[sensors[s]].left;
        }
        
        return total;
    }
    else {
        
        if (s == e)
        {
            return 0;
        }
        else if (e - s == 1)
        {
            return diff[sensors[e]].left;
        }
        
        int min = 2147483647;
        mNode* now;
        mNode* minNode = NULL;
        int NodeNum = 0;
        
        for (int i = s; i < e; i++)
        {
            if (i == 0) continue;
            now = &diff[sensors[i]];
//            cout << now->left + now->right;
            if (min > now->left + now->right)
            {
                min = now->left + now->right;
                minNode = now;
                NodeNum = i;
            }
            
        }
        k--;
        // 1 3 6 7 9
        // 2 3 1 2
        // 2 5 4 3 2
//        cout << endl << "min : " << min << ", " << NodeNum << ", " << sensors[NodeNum] << endl;
        
        int m = diff[sensors[NodeNum]].left + diff[sensors[NodeNum]].right;
        int l = installrecv(s, NodeNum-2, k, diff, sensors);
        int r = installrecv(NodeNum + 2, e,k, diff, sensors);
        
//        cout << s << e << "item = " << sensors[NodeNum] << " sum = " << diff[sensors[NodeNum]].left << "+" << diff[sensors[NodeNum]].right << " total = " << l + r + m << endl;
        
        return l + r + m;
    }
}


