using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DragDrop : MonoBehaviour
{
    //скрипт не має нічого робити із запуском гри, тож відповідна функція відсутня
    private bool is_dragging = false; //змінна чи переміщується карта (спочатку ні)
    private GameObject dropzone; //зона де можна поставить карту (потім розділити на ближній середній і дальній бій)
    private bool is_over_dropzone = false; //змінна карта над зоною доставки (спочатку ні) (потім розділити по властивостям карти)
    private Vector2 startPosition; // змінна що зберігає координати карти до руху

    public GameObject PlayerMelee; //зони куди можна класти карти
    public GameObject PlayerMiddle;
    public GameObject PlayerRear;

    public GameObject CardPlayerMelee; //карти гравця
    public GameObject CardPlayerMiddle;
    public GameObject CardPlayerRear;

    // Update is called once per frame
    void Update()
    {
        if (is_dragging) //кожен кадр йде перевірка на активацію руху
        {
            transform.position = new Vector2(Input.mousePosition.x, Input.mousePosition.y); //оновлення координат за позицією курсора
        }
    }

    private void OnCollisionEnter2D(Collision2D collision) //функція коли є колізія між двома обʼєктами
    { 
        is_over_dropzone = true; //кажемо що карту можна закріпити над обʼєктом, що який це дозволяє
        dropzone = collision.gameObject; //зберігаємо зону
    }

    private void OnCollisionExit2D(Collision2D other) //функція коли колізія між двома обʼєктами припиняється
    {
        is_over_dropzone = false; //карта більше не може бути прикріпленою
        dropzone = null; //очищаємо змінну
    }

    public void StartDrag() //функція-перемикач
    {
        startPosition = transform.position; //записуємо координати у змінну
        is_dragging = true; //починається рух
    }

    public void EndDrag() //функція-перемикач
    {
        is_dragging = false; //завершується рух
        if (is_over_dropzone) //якщо карта переміщена у правильну зону
        {
            Debug.Log(dropzone);
            Debug.Log(transform.name);
            if (dropzone == PlayerMelee && transform.name == "CardPlayerMelee(Clone)") 
            {
                transform.SetParent(dropzone.transform, false); //закріпити в рядку
            }
            else if (dropzone == PlayerMiddle && transform.name == "CardPlayerMiddle(Clone)")
            {
                transform.SetParent(dropzone.transform, false); //закріпити в рядку
            }
            else if (dropzone == PlayerRear && transform.name == "CardPlayerRear(Clone)")
            {
                transform.SetParent(dropzone.transform, false); //закріпити в рядку
            }
            else
            {
                transform.position = startPosition; //повернути назад
            }
        }
        else
        {
            transform.position = startPosition; //повернути назад
        }
    }
}
