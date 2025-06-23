
package com.example.confirmationservice.config;

import org.springframework.boot.web.servlet.ServletRegistrationBean;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.ws.transport.http.MessageDispatcherServlet;
import org.springframework.xml.xsd.SimpleXsdSchema;
import org.springframework.xml.xsd.XsdSchema;

import org.springframework.ws.wsdl.wsdl11.DefaultWsdl11Definition;

@Configuration
public class WebServiceConfig {
    @Bean
    public ServletRegistrationBean<MessageDispatcherServlet> messageDispatcherServlet(ApplicationContext context) {
        MessageDispatcherServlet servlet = new MessageDispatcherServlet();
        servlet.setApplicationContext(context);
        servlet.setTransformWsdlLocations(true);
        return new ServletRegistrationBean<>(servlet, "/ws/*");
    }

    @Bean(name = "confirmation")
    public DefaultWsdl11Definition defaultWsdl11Definition(XsdSchema confirmationSchema) {
        DefaultWsdl11Definition wsdl11Definition = new DefaultWsdl11Definition();
        wsdl11Definition.setPortTypeName("ConfirmationPort");
        wsdl11Definition.setLocationUri("/ws");
        wsdl11Definition.setTargetNamespace("http://example.com/confirmationservice");
        wsdl11Definition.setSchema(confirmationSchema);
        return wsdl11Definition;
    }

    @Bean
    public XsdSchema confirmationSchema() {
        return new SimpleXsdSchema(new org.springframework.core.io.ClassPathResource("confirmation.xsd"));
    }
}
