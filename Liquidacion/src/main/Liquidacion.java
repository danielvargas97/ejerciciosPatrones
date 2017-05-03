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
public abstract class Liquidacion {
    Liquidacion liquidacion;
    public abstract void liquidar(int opc);
    
    public Liquidacion sucesor(){
        return liquidacion;
    }
    
    public void setSucesor(Liquidacion lq){
        this.liquidacion = lq;
    }
            
}
