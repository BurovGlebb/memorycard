using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Trampoline : MonoBehaviour
{
    private void OnTriggerEnter(Collider other)
    {
        //Увеличение прыжка
        other.GetComponent<Jump>().jumpStrength *= 2;
    }
    private void OnTriggerExit(Collider other)
    {
        //Возвращение обычного прыжка
        other.GetComponent<Jump>().jumpStrength /= 2;
       
    }



}
