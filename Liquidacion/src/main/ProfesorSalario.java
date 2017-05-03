/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package main;

/**
 *
 * @author Estudiantes
 */
public class ProfesorSalario extends Liquidacion{

    @Override
    public void liquidar(int opc) {
       if(opc==4){
           System.out.println("Liquidando a profesor con salario");
       }else{
           liquidacion.liquidar(opc);
       }
    }

    
}
