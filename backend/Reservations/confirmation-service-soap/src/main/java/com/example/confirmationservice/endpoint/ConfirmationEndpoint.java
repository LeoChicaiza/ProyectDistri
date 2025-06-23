
package com.example.confirmationservice.endpoint;

import org.springframework.ws.server.endpoint.annotation.Endpoint;
import org.springframework.ws.server.endpoint.annotation.PayloadRoot;
import org.springframework.ws.server.endpoint.annotation.RequestPayload;
import org.springframework.ws.server.endpoint.annotation.ResponsePayload;

import javax.xml.bind.annotation.XmlRootElement;

@Endpoint
public class ConfirmationEndpoint {
    private static final String NAMESPACE_URI = "http://example.com/confirmationservice";

    @PayloadRoot(namespace = NAMESPACE_URI, localPart = "ConfirmationRequest")
    @ResponsePayload
    public ConfirmationResponse confirm(@RequestPayload ConfirmationRequest request) {
        ConfirmationResponse response = new ConfirmationResponse();
        response.setStatus("confirmed");
        response.setReservationId(request.getReservationId());
        return response;
    }
}

@XmlRootElement(namespace = "http://example.com/confirmationservice")
class ConfirmationRequest {
    private String reservationId;

    public String getReservationId() { return reservationId; }
    public void setReservationId(String reservationId) { this.reservationId = reservationId; }
}

@XmlRootElement(namespace = "http://example.com/confirmationservice")
class ConfirmationResponse {
    private String reservationId;
    private String status;

    public String getReservationId() { return reservationId; }
    public void setReservationId(String reservationId) { this.reservationId = reservationId; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}
