/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package main;

import java.util.Scanner;

/**
 *
 * @author Estudiantes
 */
public class Launcher {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int opc;
        Liquidacion tipo[] = new Liquidacion[5];
        tipo[0] = new ProfesorHonorario();
        tipo[1] = new ProfesorHoraCatedra();
        tipo[2] = new ProfesorPlanta();
        tipo[3] = new ProfesorSalario();
        tipo[4] = new ProfesorDefault();
        
        

        System.out.println("Ingrese una opcion para liquidar");
        System.out.println("1. Profesor con honrario");
        System.out.println("2. Profesor con hora-catedra");
        System.out.println("3. Profesor de planta");
        System.out.println("4. Profesor con salario");
    
        opc = sc.nextInt();
        
        for(int i =0;i<tipo.length-1;i++){
            tipo[i].setSucesor(tipo[i+1]);
        }
        
        tipo[0].liquidar(opc);
       
        
    }
    
}
