using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DrawCards : MonoBehaviour
{
    public GameObject CardPlayerMelee; //карти гравця
    public GameObject CardPlayerMiddle;
    public GameObject CardPlayerRear;
    public GameObject CardEnemy; //карта супротивника
    public GameObject PlayerArea; //зона гравця куди кладяться карти
    public GameObject EnemyArea; //зона супротивника

    List<GameObject> cards = new List<GameObject>(); //змінна списку кард що є у грі (спільна колода - потім розділити, створивши нову)

    // Start is called before the first frame update
    void Start() //під час запуску гри
    {
        cards.Add(CardPlayerMelee); //додаємо карти до колоди
        cards.Add(CardPlayerMiddle);
        cards.Add(CardPlayerRear);

        //зараз одразу створюються по 10 карток, потім переробити в окрему функцію що викликається після підготовки стартової колоди
        for (var i = 0; i < 10; i++) //вказана кількість карт що генеруються
        {
            GameObject playerCard = Instantiate(cards[Random.Range(0, cards.Count)], new Vector3(0, 0, 0), Quaternion.identity); //створюється карта з колоди як обʼєкт гри
            playerCard.transform.SetParent(PlayerArea.transform, false); //місцезнаходження карти в загальній ієрархії (своїй зоні)

            GameObject enemyrCard = Instantiate(CardEnemy, new Vector3(0, 0, 0), Quaternion.identity); //карти супротивника поки що мають тільки спину
            enemyrCard.transform.SetParent(EnemyArea.transform, false);
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}